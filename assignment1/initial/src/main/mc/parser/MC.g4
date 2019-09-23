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

// Parser

program  : mctype 'main' LB exp? RB multiscope EOF ;

mctype: INTTYPE | VOIDTYPE | BOOLTYPE | FLOATTYPE | STRINGTYPE;

body: (funcall | val_declare)+;

multiscope: LP content multiscope content RP| content scope content;

scope: LP content RP;

content: (funcall | val_declare | arr_declare)*;

exp: funcall | INTLIT | FLOATLIT | STRINGLIT | BOOLLIT;

funcall: ID LB exp? RB SEMI;

val_type: INTTYPE | BOOLTYPE | FLOATTYPE | STRINGTYPE;

val_declare: val_type ID (COMMA ID)* SEMI;

arr_declare: val_type ID LS INTLIT RS (COMMA ID LS INTLIT RS)* SEMI;

//Lexer

INTTYPE: 'int' ;

VOIDTYPE: 'void' ;

BOOLTYPE: 'boolean' ;

FLOATTYPE: 'float' ;

STRINGTYPE: 'string' ;

KEYWORD: 'break'|'continue'|'else'|'for'|'if'|'return'|'do'|'while' ;

fragment Digit: [0-9];

fragment Expo: [eE][-]?Digit+ ;

fragment Frac: Digit+'.'Digit* | Digit*'.'Digit+ ;

FLOATLIT: Frac Expo? | Digit+ Expo;

//FLOATLIT: [0-9]+([.][0-9]+)?[eE][-]?[0-9]+|[0-9]+[.][0-9]*|[.][0-9]+([eE][-]?[0-9]+)? ;

INTLIT: [0-9]+;

BOOLLIT: 'true'|'false' ;

//STRINGLIT: ([^"']+);

//fragment Quote: '"';

//STRINGLIT: ('?'':'Quote) ([^Quote\]|\.)* (?:Quote) ;


#STRINGLIT: QUOTE (ESC|.)*? QUOTE ;

#fragment QUOTE: [\"] -> skip;

#fragment
#ESC : '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\"' | '\\\\';

STRING:                 <skip>'\'' (~'\'' | '\'\'')* <skip>'\'';

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