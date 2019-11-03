# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\2\3\2\5\2\27\n\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\4\7\4!\n\4\f\4\16\4$\13\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5+\n\5\3\6\3\6\3\6\5\6\60\n\6\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\7\b:\n\b\f\b\16\b=\13\b\3\b\3\b\3\b")
        buf.write("\2\2\t\2\4\6\b\n\f\16\2\4\3\2\4\b\4\2\4\4\6\b\2A\2\20")
        buf.write("\3\2\2\2\4\33\3\2\2\2\6\35\3\2\2\2\b*\3\2\2\2\n,\3\2\2")
        buf.write("\2\f\63\3\2\2\2\16\65\3\2\2\2\20\21\5\4\3\2\21\22\7\3")
        buf.write("\2\2\22\23\7\24\2\2\23\24\7\25\2\2\24\26\7\26\2\2\25\27")
        buf.write("\5\6\4\2\26\25\3\2\2\2\26\27\3\2\2\2\27\30\3\2\2\2\30")
        buf.write("\31\7\27\2\2\31\32\7\2\2\3\32\3\3\2\2\2\33\34\t\2\2\2")
        buf.write("\34\5\3\2\2\2\35\36\5\n\6\2\36\"\7\30\2\2\37!\5\16\b\2")
        buf.write(" \37\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\7\3\2\2")
        buf.write("\2$\"\3\2\2\2%+\5\n\6\2&+\7\13\2\2\'+\7\n\2\2(+\7\r\2")
        buf.write("\2)+\7\f\2\2*%\3\2\2\2*&\3\2\2\2*\'\3\2\2\2*(\3\2\2\2")
        buf.write("*)\3\2\2\2+\t\3\2\2\2,-\7\16\2\2-/\7\24\2\2.\60\5\b\5")
        buf.write("\2/.\3\2\2\2/\60\3\2\2\2\60\61\3\2\2\2\61\62\7\25\2\2")
        buf.write("\62\13\3\2\2\2\63\64\t\3\2\2\64\r\3\2\2\2\65\66\5\f\7")
        buf.write("\2\66;\7\16\2\2\678\7\31\2\28:\7\16\2\29\67\3\2\2\2:=")
        buf.write("\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3\2\2\2>?\7\30")
        buf.write("\2\2?\17\3\2\2\2\7\26\"*/;")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'int'", "'void'", "'boolean'", 
                     "'float'", "'string'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'['", "']'", "'('", "')'", 
                     "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INTTYPE", "VOIDTYPE", "BOOLTYPE", 
                      "FLOATTYPE", "STRINGTYPE", "KEYWORD", "FLOATLIT", 
                      "INTLIT", "BOOLLIT", "STRINGLIT", "ID", "COMMENT", 
                      "COMMENTMULTI", "OPERATOR", "LS", "RS", "LB", "RB", 
                      "LP", "RP", "SEMI", "COMMA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mctype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4
    RULE_val_type = 5
    RULE_val_declare = 6

    ruleNames =  [ "program", "mctype", "body", "exp", "funcall", "val_type", 
                   "val_declare" ]

    EOF = Token.EOF
    T__0=1
    INTTYPE=2
    VOIDTYPE=3
    BOOLTYPE=4
    FLOATTYPE=5
    STRINGTYPE=6
    KEYWORD=7
    FLOATLIT=8
    INTLIT=9
    BOOLLIT=10
    STRINGLIT=11
    ID=12
    COMMENT=13
    COMMENTMULTI=14
    OPERATOR=15
    LS=16
    RS=17
    LB=18
    RB=19
    LP=20
    RP=21
    SEMI=22
    COMMA=23
    WS=24
    ERROR_CHAR=25
    UNCLOSE_STRING=26
    ILLEGAL_ESCAPE=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mctype(self):
            return self.getTypedRuleContext(MCParser.MctypeContext,0)


        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(MCParser.BodyContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.mctype()
            self.state = 15
            self.match(MCParser.T__0)
            self.state = 16
            self.match(MCParser.LB)
            self.state = 17
            self.match(MCParser.RB)
            self.state = 18
            self.match(MCParser.LP)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.ID:
                self.state = 19
                self.body()


            self.state = 22
            self.match(MCParser.RP)
            self.state = 23
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MctypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def BOOLTYPE(self):
            return self.getToken(MCParser.BOOLTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_mctype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMctype" ):
                return visitor.visitMctype(self)
            else:
                return visitor.visitChildren(self)




    def mctype(self):

        localctx = MCParser.MctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mctype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.VOIDTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MCParser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def val_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Val_declareContext)
            else:
                return self.getTypedRuleContext(MCParser.Val_declareContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MCParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.funcall()
            self.state = 28
            self.match(MCParser.SEMI)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 29
                self.val_declare()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MCParser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MCParser.BOOLLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MCParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.funcall()
                pass
            elif token in [MCParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(MCParser.INTLIT)
                pass
            elif token in [MCParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.match(MCParser.FLOATLIT)
                pass
            elif token in [MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.match(MCParser.STRINGLIT)
                pass
            elif token in [MCParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.match(MCParser.BOOLLIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MCParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(MCParser.ID)
            self.state = 43
            self.match(MCParser.LB)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.FLOATLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.ID))) != 0):
                self.state = 44
                self.exp()


            self.state = 47
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def BOOLTYPE(self):
            return self.getToken(MCParser.BOOLTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_val_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_type" ):
                return visitor.visitVal_type(self)
            else:
                return visitor.visitChildren(self)




    def val_type(self):

        localctx = MCParser.Val_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_val_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def val_type(self):
            return self.getTypedRuleContext(MCParser.Val_typeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.ID)
            else:
                return self.getToken(MCParser.ID, i)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_val_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_declare" ):
                return visitor.visitVal_declare(self)
            else:
                return visitor.visitChildren(self)




    def val_declare(self):

        localctx = MCParser.Val_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_val_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.val_type()
            self.state = 52
            self.match(MCParser.ID)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 53
                self.match(MCParser.COMMA)
                self.state = 54
                self.match(MCParser.ID)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





