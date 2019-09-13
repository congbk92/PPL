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

mctype: INTTYPE | VOIDTYPE | BOOLTYPE | FLOATTYPE;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

VOIDTYPE: 'void' ;

BOOLTYPE: 'boolean' ;

FLOATTYPE: 'float' ;

KEYWORD: 'break'|'continue'|'else'|'for'|'if'|'return'|'do'|'while'|'true'|'false'|'string' ;

ID: [_a-zA-Z][_a-zA-Z0-9]*;

COMMENT: '//'~'\n'* -> skip; //skip single line comment

COMMENTMULTI: '/*'.*'*/' -> skip; //skip multiline comment


OPERATOR: '+'|'-'|'*'|'/'|'!'|'%'|'||'|'&&'|'!='|'=='|'<'|'>'|'<='|'>='|'=' ;

INTLIT: [0-9]+;

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