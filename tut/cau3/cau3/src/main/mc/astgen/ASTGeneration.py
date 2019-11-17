from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
import functools 

class ASTGeneration(MCVisitor):
    #exp: term COMPARE term | term ; # COMPARE is none-association
    def visitExp(self,ctx:MCParser.ExpContext):
        return Binary(ctx.COMPARE().getText(),self.visit(ctx.term(0)),self.visit(ctx.term(1))) if ctx.COMPARE() else self.visit(ctx.term(0))
    #term: factor EXPONENT term | factor ; 
    def visitTerm(self,ctx:MCParser.TermContext):
        return Binary(ctx.EXPONENT().getText(),self.visit(ctx.factor()),self.visit(ctx.term())) if ctx.EXPONENT() else self.visit(ctx.factor())
    #factor: operand (ANDOR operand)* ;  # ANDOR is left-association
    def visitFactor(self,ctx:MCParser.FactorContext):
        rl = ctx.operand()[::-1]
        cl = zip(ctx.ANDOR()[::-1],rl[1:])
        dl = zip(ctx.ANDOR(),ctx.operand()[1:])
        '''
        exp = self.visit(rl[0])
        for node in cl:
            exp = Binary(node[0].getText(),exp,self.visit(node[1]))
        return exp
        '''
        #return Binary(ctx.ANDOR(0).getText(),self.visit(ctx.operand(0)),functools.reduce(lambda a,b : Binary(a[0].getText(),self.visit(a[1]),self.visit(b[1])),dl,self.visit(ctx.operand(0))))
        #return functools.reduce(lambda a,b : Binary(a[0].getText(),self.visit(a[1]),self.visit(b[1])),cl,self.visit(cl[0][1]))
    #operand: INTLIT | BOOLIT | LB exp RB ;
    def visitOperand(self,ctx:MCParser.OperandContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp())
        elif ctx.INTLIT():
            return IntLit(int(ctx.INTLIT().getText()))
        else:
            return BoolLit(ctx.BOOLIT().getText() == 'true')

#factor: operand (ANDOR operand)* ;