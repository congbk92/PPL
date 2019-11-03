# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\35")
        buf.write("\u011f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b")
        buf.write("\u0080\n\b\3\t\6\t\u0083\n\t\r\t\16\t\u0084\3\t\5\t\u0088")
        buf.write("\n\t\3\t\6\t\u008b\n\t\r\t\16\t\u008c\5\t\u008f\n\t\3")
        buf.write("\t\3\t\5\t\u0093\n\t\3\t\6\t\u0096\n\t\r\t\16\t\u0097")
        buf.write("\3\t\6\t\u009b\n\t\r\t\16\t\u009c\3\t\3\t\7\t\u00a1\n")
        buf.write("\t\f\t\16\t\u00a4\13\t\3\t\3\t\6\t\u00a8\n\t\r\t\16\t")
        buf.write("\u00a9\3\t\3\t\5\t\u00ae\n\t\3\t\6\t\u00b1\n\t\r\t\16")
        buf.write("\t\u00b2\5\t\u00b5\n\t\5\t\u00b7\n\t\3\n\6\n\u00ba\n\n")
        buf.write("\r\n\16\n\u00bb\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00c7\n\13\3\f\3\f\7\f\u00cb\n\f\f\f\16\f\u00ce")
        buf.write("\13\f\3\f\3\f\3\r\3\r\7\r\u00d4\n\r\f\r\16\r\u00d7\13")
        buf.write("\r\3\16\3\16\3\16\3\16\7\16\u00dd\n\16\f\16\16\16\u00e0")
        buf.write("\13\16\3\16\3\16\3\17\3\17\3\17\3\17\7\17\u00e8\n\17\f")
        buf.write("\17\16\17\u00eb\13\17\3\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u0101\n\20\3\21\3\21\3\22\3\22\3")
        buf.write("\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\6\31\u0114\n\31\r\31\16\31\u0115\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\u00e9\2\35\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\35\3\2\f\3\2\62;\3\2\60\60\4\2GGgg\3\2//")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\3\2\f\f\7\2##\'\',-//\61\61")
        buf.write("\4\2>>@@\5\2\13\f\17\17\"\"\2\u0142\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\39\3\2\2")
        buf.write("\2\5>\3\2\2\2\7B\3\2\2\2\tG\3\2\2\2\13O\3\2\2\2\rU\3\2")
        buf.write("\2\2\17\177\3\2\2\2\21\u00b6\3\2\2\2\23\u00b9\3\2\2\2")
        buf.write("\25\u00c6\3\2\2\2\27\u00c8\3\2\2\2\31\u00d1\3\2\2\2\33")
        buf.write("\u00d8\3\2\2\2\35\u00e3\3\2\2\2\37\u0100\3\2\2\2!\u0102")
        buf.write("\3\2\2\2#\u0104\3\2\2\2%\u0106\3\2\2\2\'\u0108\3\2\2\2")
        buf.write(")\u010a\3\2\2\2+\u010c\3\2\2\2-\u010e\3\2\2\2/\u0110\3")
        buf.write("\2\2\2\61\u0113\3\2\2\2\63\u0119\3\2\2\2\65\u011b\3\2")
        buf.write("\2\2\67\u011d\3\2\2\29:\7o\2\2:;\7c\2\2;<\7k\2\2<=\7p")
        buf.write("\2\2=\4\3\2\2\2>?\7k\2\2?@\7p\2\2@A\7v\2\2A\6\3\2\2\2")
        buf.write("BC\7x\2\2CD\7q\2\2DE\7k\2\2EF\7f\2\2F\b\3\2\2\2GH\7d\2")
        buf.write("\2HI\7q\2\2IJ\7q\2\2JK\7n\2\2KL\7g\2\2LM\7c\2\2MN\7p\2")
        buf.write("\2N\n\3\2\2\2OP\7h\2\2PQ\7n\2\2QR\7q\2\2RS\7c\2\2ST\7")
        buf.write("v\2\2T\f\3\2\2\2UV\7u\2\2VW\7v\2\2WX\7t\2\2XY\7k\2\2Y")
        buf.write("Z\7p\2\2Z[\7i\2\2[\16\3\2\2\2\\]\7d\2\2]^\7t\2\2^_\7g")
        buf.write("\2\2_`\7c\2\2`\u0080\7m\2\2ab\7e\2\2bc\7q\2\2cd\7p\2\2")
        buf.write("de\7v\2\2ef\7k\2\2fg\7p\2\2gh\7w\2\2h\u0080\7g\2\2ij\7")
        buf.write("g\2\2jk\7n\2\2kl\7u\2\2l\u0080\7g\2\2mn\7h\2\2no\7q\2")
        buf.write("\2o\u0080\7t\2\2pq\7k\2\2q\u0080\7h\2\2rs\7t\2\2st\7g")
        buf.write("\2\2tu\7v\2\2uv\7w\2\2vw\7t\2\2w\u0080\7p\2\2xy\7f\2\2")
        buf.write("y\u0080\7q\2\2z{\7y\2\2{|\7j\2\2|}\7k\2\2}~\7n\2\2~\u0080")
        buf.write("\7g\2\2\177\\\3\2\2\2\177a\3\2\2\2\177i\3\2\2\2\177m\3")
        buf.write("\2\2\2\177p\3\2\2\2\177r\3\2\2\2\177x\3\2\2\2\177z\3\2")
        buf.write("\2\2\u0080\20\3\2\2\2\u0081\u0083\t\2\2\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0087\3\2\2\2\u0086\u0088\t\3\2\2")
        buf.write("\u0087\u0086\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u008e\3")
        buf.write("\2\2\2\u0089\u008b\t\2\2\2\u008a\u0089\3\2\2\2\u008b\u008c")
        buf.write("\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write("\u008f\3\2\2\2\u008e\u008a\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\u0090\3\2\2\2\u0090\u0092\t\4\2\2\u0091\u0093\t")
        buf.write("\5\2\2\u0092\u0091\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0095")
        buf.write("\3\2\2\2\u0094\u0096\t\2\2\2\u0095\u0094\3\2\2\2\u0096")
        buf.write("\u0097\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u00b7\3\2\2\2\u0099\u009b\t\2\2\2\u009a\u0099\3")
        buf.write("\2\2\2\u009b\u009c\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a2\t\3\2\2\u009f")
        buf.write("\u00a1\t\2\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a4\3\2\2\2")
        buf.write("\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00b7\3")
        buf.write("\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a7\t\3\2\2\u00a6\u00a8")
        buf.write("\t\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00b4\3\2\2\2")
        buf.write("\u00ab\u00ad\t\4\2\2\u00ac\u00ae\t\5\2\2\u00ad\u00ac\3")
        buf.write("\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00b1")
        buf.write("\t\2\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b5\3\2\2\2")
        buf.write("\u00b4\u00ab\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b7\3")
        buf.write("\2\2\2\u00b6\u0082\3\2\2\2\u00b6\u009a\3\2\2\2\u00b6\u00a5")
        buf.write("\3\2\2\2\u00b7\22\3\2\2\2\u00b8\u00ba\t\2\2\2\u00b9\u00b8")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb")
        buf.write("\u00bc\3\2\2\2\u00bc\24\3\2\2\2\u00bd\u00be\7v\2\2\u00be")
        buf.write("\u00bf\7t\2\2\u00bf\u00c0\7w\2\2\u00c0\u00c7\7g\2\2\u00c1")
        buf.write("\u00c2\7h\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7n\2\2\u00c4")
        buf.write("\u00c5\7u\2\2\u00c5\u00c7\7g\2\2\u00c6\u00bd\3\2\2\2\u00c6")
        buf.write("\u00c1\3\2\2\2\u00c7\26\3\2\2\2\u00c8\u00cc\7$\2\2\u00c9")
        buf.write("\u00cb\t\3\2\2\u00ca\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2")
        buf.write("\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cf\3")
        buf.write("\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\7$\2\2\u00d0\30")
        buf.write("\3\2\2\2\u00d1\u00d5\t\6\2\2\u00d2\u00d4\t\7\2\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2")
        buf.write("\u00d5\u00d6\3\2\2\2\u00d6\32\3\2\2\2\u00d7\u00d5\3\2")
        buf.write("\2\2\u00d8\u00d9\7\61\2\2\u00d9\u00da\7\61\2\2\u00da\u00de")
        buf.write("\3\2\2\2\u00db\u00dd\n\b\2\2\u00dc\u00db\3\2\2\2\u00dd")
        buf.write("\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df\u00e1\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e2\b")
        buf.write("\16\2\2\u00e2\34\3\2\2\2\u00e3\u00e4\7\61\2\2\u00e4\u00e5")
        buf.write("\7,\2\2\u00e5\u00e9\3\2\2\2\u00e6\u00e8\13\2\2\2\u00e7")
        buf.write("\u00e6\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00e9\u00e7\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00e9\3")
        buf.write("\2\2\2\u00ec\u00ed\7,\2\2\u00ed\u00ee\7\61\2\2\u00ee\u00ef")
        buf.write("\3\2\2\2\u00ef\u00f0\b\17\2\2\u00f0\36\3\2\2\2\u00f1\u0101")
        buf.write("\t\t\2\2\u00f2\u00f3\7~\2\2\u00f3\u0101\7~\2\2\u00f4\u00f5")
        buf.write("\7(\2\2\u00f5\u0101\7(\2\2\u00f6\u00f7\7#\2\2\u00f7\u0101")
        buf.write("\7?\2\2\u00f8\u00f9\7?\2\2\u00f9\u0101\7?\2\2\u00fa\u0101")
        buf.write("\t\n\2\2\u00fb\u00fc\7>\2\2\u00fc\u0101\7?\2\2\u00fd\u00fe")
        buf.write("\7@\2\2\u00fe\u0101\7?\2\2\u00ff\u0101\7?\2\2\u0100\u00f1")
        buf.write("\3\2\2\2\u0100\u00f2\3\2\2\2\u0100\u00f4\3\2\2\2\u0100")
        buf.write("\u00f6\3\2\2\2\u0100\u00f8\3\2\2\2\u0100\u00fa\3\2\2\2")
        buf.write("\u0100\u00fb\3\2\2\2\u0100\u00fd\3\2\2\2\u0100\u00ff\3")
        buf.write("\2\2\2\u0101 \3\2\2\2\u0102\u0103\7]\2\2\u0103\"\3\2\2")
        buf.write("\2\u0104\u0105\7_\2\2\u0105$\3\2\2\2\u0106\u0107\7*\2")
        buf.write("\2\u0107&\3\2\2\2\u0108\u0109\7+\2\2\u0109(\3\2\2\2\u010a")
        buf.write("\u010b\7}\2\2\u010b*\3\2\2\2\u010c\u010d\7\177\2\2\u010d")
        buf.write(",\3\2\2\2\u010e\u010f\7=\2\2\u010f.\3\2\2\2\u0110\u0111")
        buf.write("\7.\2\2\u0111\60\3\2\2\2\u0112\u0114\t\13\2\2\u0113\u0112")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0113\3\2\2\2\u0115")
        buf.write("\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\b\31\2")
        buf.write("\2\u0118\62\3\2\2\2\u0119\u011a\13\2\2\2\u011a\64\3\2")
        buf.write("\2\2\u011b\u011c\13\2\2\2\u011c\66\3\2\2\2\u011d\u011e")
        buf.write("\13\2\2\2\u011e8\3\2\2\2\31\2\177\u0084\u0087\u008c\u008e")
        buf.write("\u0092\u0097\u009c\u00a2\u00a9\u00ad\u00b2\u00b4\u00b6")
        buf.write("\u00bb\u00c6\u00cc\u00d5\u00de\u00e9\u0100\u0115\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    BOOLTYPE = 4
    FLOATTYPE = 5
    STRINGTYPE = 6
    KEYWORD = 7
    FLOATLIT = 8
    INTLIT = 9
    BOOLLIT = 10
    STRINGLIT = 11
    ID = 12
    COMMENT = 13
    COMMENTMULTI = 14
    OPERATOR = 15
    LS = 16
    RS = 17
    LB = 18
    RB = 19
    LP = 20
    RP = 21
    SEMI = 22
    COMMA = 23
    WS = 24
    ERROR_CHAR = 25
    UNCLOSE_STRING = 26
    ILLEGAL_ESCAPE = 27

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'boolean'", "'float'", "'string'", 
            "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "BOOLTYPE", "FLOATTYPE", "STRINGTYPE", 
            "KEYWORD", "FLOATLIT", "INTLIT", "BOOLLIT", "STRINGLIT", "ID", 
            "COMMENT", "COMMENTMULTI", "OPERATOR", "LS", "RS", "LB", "RB", 
            "LP", "RP", "SEMI", "COMMA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "BOOLTYPE", "FLOATTYPE", 
                  "STRINGTYPE", "KEYWORD", "FLOATLIT", "INTLIT", "BOOLLIT", 
                  "STRINGLIT", "ID", "COMMENT", "COMMENTMULTI", "OPERATOR", 
                  "LS", "RS", "LB", "RB", "LP", "RP", "SEMI", "COMMA", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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


