grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
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

expr: boolExpr | intExpr | floatExpr | stringExpr| indexExpr | invocExpr ;

boolExpr: varialble ASSIGN boolExpr | boolExpr1 ;
boolExpr1:  boolExpr1  OR boolExpr2 | boolExpr2 ;
boolExpr2: boolExpr2 AND boolExpr3 | boolExpr3 ;
boolExpr3: boolExpr4 ( EQ | DIF ) boolExpr4 | intExpr ( EQ | DIF ) intExpr | boolExpr4 ;
boolExpr4: (intExpr|floatExpr)( BIG | BIGEQ | LESS | LESSEQ )(intExpr|floatExpr) | boolExpr5 ;
boolExpr5: NOT boolExpr5  | boolExpr6 ;
boolExpr6: indexExpr | boolExpr7 ;
boolExpr7: LB boolExpr RB | BOOLEANLIT | ID | invocExpr ;

intExpr: varialble ASSIGN intExpr | intExpr1 ;
intExpr1: intExpr1 ( ADD | SUB ) intExpr2 | intExpr2 ;
intExpr2: intExpr2 (MUL | DIV | MOD ) intExpr3 | intExpr3 ;
intExpr3: SUB intExpr3 | intExpr4 ;
intExpr4: indexExpr | intExpr5 ;
intExpr5: LB intExpr RB | INTLIT | ID | invocExpr ;

floatExpr: varialble ASSIGN floatExpr | floatExpr1 ;
floatExpr1: floatExpr1 (ADD | SUB) floatExpr2 | floatExpr2 ;
floatExpr2: floatExpr2 (MUL | DIV) floatExpr3 | floatExpr3 ;
floatExpr3: SUB floatExpr3 | floatExpr4 ;
floatExpr4: indexExpr | floatExpr5 ;
floatExpr5: LB (floatExpr | intExpr) RB | INTLIT | FLOATLIT | ID | invocExpr ;


stringExpr: varialble ASSIGN stringExpr | STRINGLIT ;

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

fragment Esc : '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\"' | '\\\\' ;

STRINGLIT: '"'(Esc|.)*?'"' ;

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

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;