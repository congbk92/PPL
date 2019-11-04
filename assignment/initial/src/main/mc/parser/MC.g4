grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.ILLEGAL_ESCAPE:
        result = super().emit().text;
        raise IllegalEscape(result[1:len(result)]);
    elif tk == self.STRINGLIT:
        tmpStr = super().emit().text;
        tmpStr = tmpStr[1:len(tmpStr)-1];
        super().emit().text = tmpStr;
        return tmpStr;
    elif tk == self.UNCLOSE_STRING:
        result = super().emit().text;
        lastPost = len(result);
        if "\n" in result:
            lastPost = lastPost - 1;
        raise UncloseString(result[1:lastPost]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
    language=Python3;
}

program: manyDecl EOF;

manyDecl: decl tailDecl ;
tailDecl: decl tailDecl | ;

decl: funcDecl | varDecl ;

varDecl: primitiveType listVar SM ;
listVar: var (CM var)* ;
var: ID (LS INTLIT RS)?;

funcDecl: mctype ID LB paramList RB body;
body: blockStmt;
mctype: primitiveType | arrayPntType | VOIDTYPE ;
paramList: paramDecl tailParamList | ;
tailParamList: CM paramDecl tailParamList | ;
paramDecl: primitiveType ID (LS RS)? ;

primitiveType: BOOLEANTYPE | INTTYPE | FLOATTYPE | STRINGTYPE ;
arrayPntType: primitiveType LS RS ;

blockStmt: LP listMemberBlock RP ;
listMemberBlock: memberBlock tailListMemberBlock | ;
tailListMemberBlock: memberBlock tailListMemberBlock | ;
memberBlock: varDecl | stmt ;

stmt: ifStmt | dowhileStmt | forStmt | breakStmt | continueStmt | returnStmt | exprStmt | blockStmt ; 
ifStmt: IF LB exp RB stmt (ELSE stmt)? ;
dowhileStmt: DO listStmt WHILE exp SM ;
listStmt: stmt+ ;
forStmt: FOR LB exp SM exp SM exp RB stmt ;
breakStmt: BREAK SM ;
continueStmt: CONTINUE SM ;
returnStmt: RETURN exp? SM ;
exprStmt: exp SM ;

exp: lhs ASSIGN exp | binaryExpr;
binaryExpr: binaryExpr OR binaryExpr1 | binaryExpr1;
binaryExpr1: binaryExpr1 AND binaryExpr2 | binaryExpr2;
binaryExpr2: binaryExpr3 (EQ | DIF) binaryExpr3 | binaryExpr3;
binaryExpr3: binaryExpr4 (BIG | BIGEQ | LESS | LESSEQ) binaryExpr4 | binaryExpr4;
binaryExpr4: binaryExpr4 (ADD | SUB) binaryExpr5 | binaryExpr5;
binaryExpr5: binaryExpr5 (MUL | DIV | MOD ) unaryExpr | unaryExpr;
unaryExpr: (SUB | NOT) unaryExpr | indexExpr | higherExpr;
indexExpr: (ID | funcall) LS exp RS;
higherExpr: LB exp RB | INTLIT | FLOATLIT| BOOLEANLIT | STRINGLIT | ID | funcall;

funcall: ID LB lisExpr RB ;
lisExpr: exp lisExprTail | ; // Nullable
lisExprTail: CM exp lisExprTail | ;
lhs: ID | indexExpr ; 

//Lexer

INTTYPE: 'int' ;

VOIDTYPE: 'void' ;

BOOLEANTYPE: 'boolean' ;

FLOATTYPE: 'float' ;

STRINGTYPE: 'string' ;

IF: 'if' ;
ELSE: 'else' ;
FOR: 'for' ;
DO: 'do' ;
WHILE: 'while' ;
BREAK: 'break' ;
CONTINUE: 'continue' ;
RETURN: 'return' ;

fragment Digit: [0-9] ;

fragment Expo: [eE][-]?Digit+ ;

fragment Frac: Digit+'.'Digit* | Digit*'.'Digit+ ;

FLOATLIT: Frac Expo? | Digit+ Expo ;

//FLOATLIT: [0-9]+([.][0-9]+)?[eE][-]?[0-9]+|[0-9]+[.][0-9]*|[.][0-9]+([eE][-]?[0-9]+)? ;

INTLIT: [0-9]+ ;

BOOLEANLIT: 'true'|'false' ;

ID: [_a-zA-Z][_a-zA-Z0-9]* ;

COMMENT: '//'~'\n'* -> skip ; //skip single line comment

COMMENTMULTI: '/*'.*?'*/' -> skip ; //skip multiline comment

ADD: '+' ;

SUB: '-' ;

MUL: '*' ;

DIV: '/' ;

NOT: '!' ;

MOD: '%' ;

OR: '||' ;

AND: '&&' ;

DIF: '!=' ;

EQ: '==' ;

BIG: '>' ;

BIGEQ: '>=' ;

LESS: '<' ;

LESSEQ: '<=' ;

ASSIGN: '=' ;

LS: '[' ;

RS: ']' ;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SM: ';' ;

CM: ',' ;

STRINGLIT: '"' ( '\\' [bfnrt"\\] | ~[\b\f\n\r\t"\\] )*? '"';

UNCLOSE_STRING: '"' ( '\\' [bfnrt"\\] | ~[\b\f\n\r\t"\\] )*? ('\n'|EOF);

ILLEGAL_ESCAPE: '"' ( '\\' [bfnrt"\\] | ~[\b\f\n\r\t"\\] )*? [\b\f\r\t\\];

WS : [ \t\f\r\n]+ -> skip ; // skip spaces, tabs, formfeed, carriage return, newlines

ERROR_CHAR: . ;