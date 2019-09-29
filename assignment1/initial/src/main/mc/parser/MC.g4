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

program: manyDecl;

manyDecl: decl tailDecl ;
tailDecl: decl tailDecl | ;

decl: funcDecl | globalVarDecl ;

globalVarDecl: varDecl ;
varDecl: primitiveType listVar SM ;
listVar: var tailListVar ;
tailListVar: CM var tailListVar | ;
var: ID | arrayDecl ;
arrayDecl: ID LS INTLIT RS ;

funcDecl: mctype ID LB paramList RB blockStmt ;
mctype: primitiveType | arrayPntType | VOIDTYPE ;
paramList: paramDecl tailParamList | ;
tailParamList: CM paramDecl tailParamList | ;
paramDecl: primitiveType ID (LS RS)? ;

primitiveType: BOOLEANTYPE | INTTYPE | FLOATTYPE | STRINGTYPE ;
arrayPntType: primitiveType LS RS ;

blockStmt: LP listMemberBlock RP ;
listMemberBlock: memberBlock taillistMemberBlock | ;
taillistMemberBlock: memberBlock taillistMemberBlock | ;
memberBlock: localVarDecl | stmt ;
localVarDecl: varDecl ;

stmt: ifStmt | dowhileStmt | forStmt | breakStmt | continueStmt | returnStmt | exprStmt | blockStmt ; 
ifStmt: IF LB boolExpr RB stmt (ELSE stmt)? ;
dowhileStmt: DO listStmt WHILE boolExpr SM ;
listStmt: stmt tailListStmt ;
tailListStmt: stmt tailListStmt | ;
forStmt: FOR LP expr SM boolExpr SM expr RP stmt ;
breakStmt: BREAK SM ;
continueStmt: CONTINUE SM ;
returnStmt: RETURN (expr) SM ;
exprStmt: expr SM ;

expr: varialble ASSIGN expr | rightExpr ;

rightExpr: boolExpr | intExpr | floatExpr | stringExpr| indexExpr | invocExpr | ID ;

boolExpr:  boolExpr  OR boolExpr2 | boolExpr2 ;
boolExpr2: boolExpr2 AND boolExpr3 | boolExpr3 ;
boolExpr3: boolExpr4 ( EQ | DIF ) boolExpr4 | intExpr ( EQ | DIF ) intExpr | boolExpr4 ;
boolExpr4: (intExpr|floatExpr)( BIG | BIGEQ | LESS | LESSEQ )(intExpr|floatExpr) | boolExpr5 ;
boolExpr5: NOT boolExpr5  | boolExpr6 ;
boolExpr6: indexExpr | boolExpr7 ;
boolExpr7: LB boolExpr RB | BOOLEANLIT | ID | invocExpr ;

intExpr: intExpr ( ADD | SUB ) intExpr2 | intExpr2 ;
intExpr2: intExpr2 (MUL | DIV | MOD ) intExpr3 | intExpr3 ;
intExpr3: SUB intExpr3 | intExpr4 ;
intExpr4: indexExpr | intExpr5 ;
intExpr5: LB intExpr RB | INTLIT | ID | invocExpr ;

floatExpr: floatExpr (ADD | SUB) floatExpr2 | floatExpr2 ;
floatExpr2: floatExpr2 (MUL | DIV) floatExpr3 | floatExpr3 ;
floatExpr3: SUB floatExpr3 | floatExpr4 ;
floatExpr4: indexExpr | floatExpr5 ;
floatExpr5: LB (floatExpr | intExpr) RB | INTLIT | FLOATLIT | ID | invocExpr ;


stringExpr: STRINGLIT ;

indexExpr: (ID | invocExpr) LS intExpr RS ;

invocExpr: ID LB lisExpr RB ;
lisExpr: expr lisExprTail | ; // Nullable
lisExprTail: CM expr lisExprTail | ;

varialble: ID | indexExpr ; 

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