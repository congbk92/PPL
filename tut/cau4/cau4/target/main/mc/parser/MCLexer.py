# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("@\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\6\4%\n\4\r\4\16\4&\3")
        buf.write("\5\3\5\3\6\6\6,\n\6\r\6\16\6-\3\7\3\7\3\b\3\b\3\t\6\t")
        buf.write("\65\n\t\r\t\16\t\66\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\2\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\3\2\5\3\2c|\3\2\62;\5\2\13\f\17\17\"\"\2B\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5\37\3\2\2\2\7$\3\2")
        buf.write("\2\2\t(\3\2\2\2\13+\3\2\2\2\r/\3\2\2\2\17\61\3\2\2\2\21")
        buf.write("\64\3\2\2\2\23:\3\2\2\2\25<\3\2\2\2\27>\3\2\2\2\31\32")
        buf.write("\7h\2\2\32\33\7n\2\2\33\34\7q\2\2\34\35\7c\2\2\35\36\7")
        buf.write("v\2\2\36\4\3\2\2\2\37 \7k\2\2 !\7p\2\2!\"\7v\2\2\"\6\3")
        buf.write("\2\2\2#%\t\2\2\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2")
        buf.write("\2\2\'\b\3\2\2\2()\7.\2\2)\n\3\2\2\2*,\t\3\2\2+*\3\2\2")
        buf.write("\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\f\3\2\2\2/\60\7]\2\2")
        buf.write("\60\16\3\2\2\2\61\62\7_\2\2\62\20\3\2\2\2\63\65\t\4\2")
        buf.write("\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2")
        buf.write("\2\2\678\3\2\2\289\b\t\2\29\22\3\2\2\2:;\13\2\2\2;\24")
        buf.write("\3\2\2\2<=\13\2\2\2=\26\3\2\2\2>?\13\2\2\2?\30\3\2\2\2")
        buf.write("\6\2&-\66\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    FLOATTYPE = 1
    INTTYPE = 2
    ID = 3
    COMMA = 4
    INTLIT = 5
    LSB = 6
    RSB = 7
    WS = 8
    ERROR_CHAR = 9
    UNCLOSE_STRING = 10
    ILLEGAL_ESCAPE = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'float'", "'int'", "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "FLOATTYPE", "INTTYPE", "ID", "COMMA", "INTLIT", "LSB", "RSB", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "FLOATTYPE", "INTTYPE", "ID", "COMMA", "INTLIT", "LSB", 
                  "RSB", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


