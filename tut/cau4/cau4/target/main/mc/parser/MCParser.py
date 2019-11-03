# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\'\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16")
        buf.write("\n\2\r\2\16\2\17\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\5\7\5\34\n\5\f\5\16\5\37\13\5\3\6\3\6\3\6\3\6\5\6%\n")
        buf.write("\6\3\6\2\2\7\2\4\6\b\n\2\3\3\2\3\4\2$\2\r\3\2\2\2\4\23")
        buf.write("\3\2\2\2\6\26\3\2\2\2\b\30\3\2\2\2\n \3\2\2\2\f\16\5\4")
        buf.write("\3\2\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2")
        buf.write("\2\2\20\21\3\2\2\2\21\22\7\2\2\3\22\3\3\2\2\2\23\24\5")
        buf.write("\6\4\2\24\25\5\b\5\2\25\5\3\2\2\2\26\27\t\2\2\2\27\7\3")
        buf.write("\2\2\2\30\35\5\n\6\2\31\32\7\6\2\2\32\34\5\n\6\2\33\31")
        buf.write("\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36")
        buf.write("\t\3\2\2\2\37\35\3\2\2\2 $\7\5\2\2!\"\7\b\2\2\"#\7\7\2")
        buf.write("\2#%\7\t\2\2$!\3\2\2\2$%\3\2\2\2%\13\3\2\2\2\5\17\35$")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'float'", "'int'", "<INVALID>", "','", 
                     "<INVALID>", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "FLOATTYPE", "INTTYPE", "ID", "COMMA", 
                      "INTLIT", "LSB", "RSB", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vardecl = 1
    RULE_mctype = 2
    RULE_manyvar = 3
    RULE_var = 4

    ruleNames =  [ "program", "vardecl", "mctype", "manyvar", "var" ]

    EOF = Token.EOF
    FLOATTYPE=1
    INTTYPE=2
    ID=3
    COMMA=4
    INTLIT=5
    LSB=6
    RSB=7
    WS=8
    ERROR_CHAR=9
    UNCLOSE_STRING=10
    ILLEGAL_ESCAPE=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VardeclContext)
            else:
                return self.getTypedRuleContext(MCParser.VardeclContext,i)


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
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.vardecl()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MCParser.FLOATTYPE or _la==MCParser.INTTYPE):
                    break

            self.state = 15
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mctype(self):
            return self.getTypedRuleContext(MCParser.MctypeContext,0)


        def manyvar(self):
            return self.getTypedRuleContext(MCParser.ManyvarContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.mctype()
            self.state = 18
            self.manyvar()
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

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_mctype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMctype" ):
                return visitor.visitMctype(self)
            else:
                return visitor.visitChildren(self)




    def mctype(self):

        localctx = MCParser.MctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mctype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            _la = self._input.LA(1)
            if not(_la==MCParser.FLOATTYPE or _la==MCParser.INTTYPE):
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


    class ManyvarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarContext)
            else:
                return self.getTypedRuleContext(MCParser.VarContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_manyvar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManyvar" ):
                return visitor.visitManyvar(self)
            else:
                return visitor.visitChildren(self)




    def manyvar(self):

        localctx = MCParser.ManyvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_manyvar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.var()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 23
                self.match(MCParser.COMMA)
                self.state = 24
                self.var()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MCParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(MCParser.ID)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 31
                self.match(MCParser.LSB)
                self.state = 32
                self.match(MCParser.INTLIT)
                self.state = 33
                self.match(MCParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





