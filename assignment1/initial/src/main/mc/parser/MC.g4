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

program  : mctype 'main' LB RB LP body? RP EOF ;

mctype: INTTYPE | VOIDTYPE | BOOLTYPE | FLOATTYPE | STRINGTYPE;

body: funcall SEMI val_declare*;

exp: funcall | INTLIT | FLOATLIT | STRINGLIT | BOOLLIT;

funcall: ID LB exp? RB ;

val_type: INTTYPE | BOOLTYPE | FLOATTYPE | STRINGTYPE;

val_declare: val_type ID (COMMA ID)* SEMI;

INTTYPE: 'int' ;

VOIDTYPE: 'void' ;

BOOLTYPE: 'boolean' ;

FLOATTYPE: 'float' ;

STRINGTYPE: 'string' ;

KEYWORD: 'break'|'continue'|'else'|'for'|'if'|'return'|'do'|'while' ;

FLOATLIT: [0-9]+([.][0-9]+)?[eE][-]?[0-9]+|[0-9]+[.][0-9]*|[.][0-9]+([eE][-]?[0-9]+)? ;

INTLIT: [0-9]+;

BOOLLIT: 'true'|'false' ;

STRINGLIT: ([^"']+);

ID: [_a-zA-Z][_a-zA-Z0-9]*;

COMMENT: '//'~'\n'* -> skip; //skip single line comment

COMMENTMULTI: '/*'.*?'*/' -> skip; //skip multiline comment

OPERATOR: '+'|'-'|'*'|'/'|'!'|'%'|'||'|'&&'|'!='|'=='|'<'|'>'|'<='|'>='|'=' ;

LS: '[' ;

RS: ']' ;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

COMMA: ',';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;