from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    #program: vardecl+ EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        lst = []
        for i in ctx.vardecl(): 
            lst = lst + self.visit(i)
        return Program(lst)

    #vardecl: mctype manyvar ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        self.mctype = self.visit(ctx.mctype()) 
        return self.visit(ctx.manyvar())
    
    #manyvar: var (COMMA var)* ;
    def visitManyvar(self,ctx:MCParser.ManyvarContext):
        return [self.visit(i) for i in ctx.var()]
  
  	#mctype: INTTYPE | FLOATTYPE ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()
    #var: ID (LSB INTLIT RSB)? ;
    def visitVar(self,ctx:MCParser.VarContext):
        if ctx.getChildCount() == 4:
            return VarDecl(ArrayType(self.mctype,int(ctx.INTLIT().getText())),ctx.ID().getText())
        else:
            return VarDecl(self.mctype,ctx.ID().getText())