from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    '''
    program: manyDecl;
    manyDecl: decl tailDecl ;
    tailDecl: decl tailDecl | ;
    '''
    def visitProgram(self,ctx:MCParser.ProgramContext):
        #return Program([FuncDecl(Id("main"),[],self.visit(ctx.mctype()),Block([self.visit(ctx.body())] if ctx.body() else []))])
        return Program(self.visit(ctx.manyDecl()))

    def visitManyDecl(self,ctx:MCParser.ManyDeclContext):
        return self.visit(ctx.decl()) + self.visit(ctx.tailDecl())
    def visitTailDecl(self,ctx:MCParser.TailDeclContext):
        return self.visit(ctx.decl()) + self.visit(ctx.tailDecl()) if ctx.decl() else []

    #    decl: funcDecl | varDecl;
    def visitDecl(self,ctx:MCParser.DeclContext):
        return [self.visit(ctx.funcDecl())] if ctx.funcDecl() else self.visit(ctx.varDecl())

    #varDecl: primitiveType listVar SM ;
    def visitVarDecl(self,ctx:MCParser.VarDeclContext):
        self.varType = self.visit(ctx.primitiveType())
        return self.visit(ctx.listVar()) 
    #listVar: var tailListVar 
    def visitListVar(self,ctx:MCParser.ListVarContext):
        return [self.visit(ctx.var())] + self.visit(ctx.tailListVar())
    #tailListVar: CM var tailListVar | ;
    def visitTailListVar(self,ctx:MCParser.TailListVarContext):
        return  [self.visit(ctx.var())] + self.visit(ctx.tailListVar()) if ctx.var() else []
    #var: ID | arrayDecl ;
    def visitVar(self,ctx:MCParser.VarContext):
        return  self.visit(ctx.arrayDecl()) if ctx.arrayDecl() else VarDecl(ctx.ID().getText(),self.varType)
    #arrayDecl: ID LS INTLIT RS;
    def visitArrayDecl(self,ctx:MCParser.VarContext):
        return VarDecl(ctx.ID().getText(),ArrayType(int(ctx.INTLIT().getText()),self.varType))
    #funcDecl: mctype ID LB paramList RB body;
    def visitFuncDecl(self,ctx:MCParser.FuncDeclContext):
        return FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.paramList()),self.visit(ctx.mctype()),self.visit(ctx.body()))

    #mctype: primitiveType | arrayPntType | VOIDTYPE ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.primitiveType():
            return self.visit(ctx.primitiveType())
        elif ctx.arrayPntType():
            return self.visit(ctx.arrayPntType())
        else:
            return VoidType
    #arrayPntType: primitiveType LS RS ;
    def visitArrayPntType(self,ctx:MCParser.ArrayPntTypeContext):
        return ArrayPointerType(self.visit(ctx.primitiveType()))
    #primitiveType: BOOLEANTYPE | INTTYPE | FLOATTYPE | STRINGTYPE ;
    def visitPrimitiveType(self,ctx:MCParser.PrimitiveTypeContext):
        if ctx.INTTYPE():
            return IntType
        elif ctx.FLOATTYPE():
            return FloatType
        elif ctx.BOOLEANTYPE():
            return BoolType
        else:
            return StringType
    ''' paramList: paramDecl tailParamList | ;
        tailParamList: CM paramDecl tailParamList | ;
    '''
    def visitParamList(self,ctx:MCParser.ParamListContext):
        return [self.visit(ctx.paramDecl())] + self.visit(ctx.tailParamList()) if ctx.paramDecl() else []
    def visitTailParamList(self,ctx:MCParser.TailParamListContext):
        return [self.visit(ctx.paramDecl())] + self.visit(ctx.tailParamList()) if ctx.paramDecl() else []
    #paramDecl: primitiveType ID (LS RS)?;
    def visitParamDecl(self,ctx:MCParser.ParamDeclContext):
        if ctx.getChildCount() == 2:
            return VarDecl(ctx.ID().getText(),self.visit(ctx.primitiveType())) 
        else:
            return VarDecl(ctx.ID().getText(),ArrayPointerType(self.visit(ctx.primitiveType())))

    def visitBody(self,ctx:MCParser.BodyContext):
        return self.visit(ctx.blockStmt())
    #blockStmt: LP listMemberBlock RP ;
    def visitBlockStmt(self,ctx:MCParser.BlockStmtContext):
        #return Block([])
        return Block(self.visit(ctx.listMemberBlock()))

    #listMemberBlock: memberBlock tailListMemberBlock | ;
    #taillistMemberBlock: memberBlock tailListMemberBlock | ;
    def visitListMemberBlock(self,ctx:MCParser.ListMemberBlockContext):
        return self.visit(ctx.memberBlock()) + self.visit(ctx.tailListMemberBlock()) if ctx.memberBlock() else []
    def visitTailListMemberBlock(self,ctx:MCParser.TailListMemberBlockContext):
        return self.visit(ctx.memberBlock()) + self.visit(ctx.tailListMemberBlock()) if ctx.memberBlock() else []
    #memberBlock: varDecl | stmt ;
    def visitMemberBlock(self,ctx:MCParser.MemberBlockContext):
        return self.visit(ctx.varDecl()) if ctx.varDecl() else [self.visit(ctx.stmt())]

    #stmt: ifStmt | dowhileStmt | forStmt | breakStmt | continueStmt | returnStmt | exprStmt | blockStmt ;
    def visitStmt(self,ctx:MCParser.StmtContext):
        if ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.dowhileStmt():
            return self.visit(ctx.dowhileStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.continueStmt():
            return self.visit(ctx.continueStmt())
        elif ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        elif ctx.exprStmt():
            return self.visit(ctx.exprStmt())
        elif ctx.blockStmt():
            return self.visit(ctx.blockStmt())
    

    #exprStmt: exp SM ;
    def visitExprStmt(self,ctx:MCParser.ExprStmtContext):
        return self.visit(ctx.exp())

    #exp: lhs ASSIGN exp | binaryExpr;
    def visitExp(self,ctx:MCParser.ExpContext):
        if ctx.ASSIGN():
            return BinaryOp(ctx.ASSIGN().getText(), self.visit(ctx.lhs()), self.visit(ctx.exp()))  
        else:
            return self.visit(ctx.binaryExpr())
    #lhs: ID | indexExpr ;
    def visitLhs(self,ctx:MCParser.LhsContext):
        return self.visit(ctx.IndexExpr()) if ctx.IndexExpr() else Id(ctx.ID().getText())
    #binaryExpr: binaryExpr OR binaryExpr1 | binaryExpr1;
    def visitBinaryExpr(self,ctx:MCParser.BinaryExprContext):
        if ctx.OR():
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.binaryExpr()), self.visit(ctx.binaryExpr1()))  
        else:
            return self.visit(ctx.binaryExpr1())
    #binaryExpr1: binaryExpr1 AND binaryExpr2 | binaryExpr2;
    def visitBinaryExpr1(self,ctx:MCParser.BinaryExpr1Context):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.binaryExpr1()), self.visit(ctx.binaryExpr2())) 
        else:
            return self.visit(ctx.binaryExpr2())
    #binaryExpr2: binaryExpr3 (EQ | DIF) binaryExpr3 | binaryExpr3;
    def visitBinaryExpr2(self,ctx:MCParser.BinaryExpr2Context):
        if ctx.EQ():
            return BinaryOp(ctx.EQ().getText(), self.visit(ctx.binaryExpr3(0)), self.visit(ctx.binaryExpr3(1)))
        elif ctx.DIF():
            return BinaryOp(ctx.DIF().getText(), self.visit(ctx.binaryExpr3(0)), self.visit(ctx.binaryExpr3(1)))
        else:
            return self.visit(ctx.binaryExpr3())
    #binaryExpr3: binaryExpr4 (BIG | BIGEQ | LESS | LESSEQ) binaryExpr4 | binaryExpr4;
    def visitBinaryExpr3(self,ctx:MCParser.BinaryExpr3Context):
        if ctx.BIG():
            return BinaryOp(ctx.BIG().getText(), self.visit(ctx.binaryExpr4(0)), self.visit(ctx.binaryExpr4(1)))
        elif ctx.BIGEQ():
            return BinaryOp(ctx.BIGEQ().getText(), self.visit(ctx.binaryExpr4(0)), self.visit(ctx.binaryExpr4(1)))
        elif ctx.LESS():
            return BinaryOp(ctx.LESS().getText(), self.visit(ctx.binaryExpr4(0)), self.visit(ctx.binaryExpr4(1)))
        elif ctx.LESSEQ():
            return BinaryOp(ctx.LESSEQ().getText(), self.visit(ctx.binaryExpr4(0)), self.visit(ctx.binaryExpr4(1)))
        else:
            return self.visit(ctx.binaryExpr4(0))
    #binaryExpr4: binaryExpr4 (ADD | SUB) binaryExpr5 | binaryExpr5;
    def visitBinaryExpr4(self,ctx:MCParser.BinaryExpr4Context):
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(), self.visit(ctx.binaryExpr4()), self.visit(ctx.binaryExpr5()))
        if ctx.SUB():
            return BinaryOp(ctx.SUB().getText(), self.visit(ctx.binaryExpr4()), self.visit(ctx.binaryExpr5())) 
        else:
            return self.visit(ctx.binaryExpr5())
    #binaryExpr5: binaryExpr5 (MUL | DIV | MOD ) unaryExpr | unaryExpr;
    def visitBinaryExpr5(self,ctx:MCParser.BinaryExpr5Context):
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), self.visit(ctx.binaryExpr5()), self.visit(ctx.unaryExpr()))
        if ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), self.visit(ctx.binaryExpr5()), self.visit(ctx.unaryExpr()))
        if ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), self.visit(ctx.binaryExpr5()), self.visit(ctx.unaryExpr())) 
        else:
            return self.visit(ctx.unaryExpr())
    #unaryExpr: (SUB | NOT) unaryExpr | indexExpr;
    def visitUnaryExpr(self,ctx:MCParser.UnaryExprContext):
        if ctx.SUB():
            return UnaryOp(ctx.SUB().getText(),self.visit(ctx.unaryExpr()));
        elif ctx.NOT():
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.unaryExpr()));
        else:
            return self.visit(ctx.indexExpr())
    #indexExpr: (ID | funcall) LS exp RS | higherExpr;
    def visitIndexExpr(self,ctx:MCParser.IndexExprContext):
        if ctx.ID():
            return ArrayCell(Id(ctx.ID().getText()),self.visit(ctx.exp()))
        elif ctx.funcall():
            return ArrayCell(self.visit(ctx.funcall()),self.visit(ctx.exp()))
        else:
            return self.visit(ctx.higherExpr())
    #higherExpr: LB exp RB | INTLIT | FLOATLIT| BOOLEANLIT | STRINGLIT | ID | funcall;
    def visitHigherExpr(self,ctx:MCParser.HigherExprContext):
        if ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLEANLIT():
            return BooleanLiteral(bool(ctx.BOOLEANLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.FLOATLIT().getText())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.funcall())
    #funcall: ID LB lisExpr RB ;
    def visitFuncall(self,ctx:MCParser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.lisExpr()))
    '''
    lisExpr: exp lisExprTail | ; // Nullable
    lisExprTail: CM exp lisExprTail | ;
    '''
    def visitLisExpr(self,ctx:MCParser.LisExprContext):
        return [self.visit(ctx.exp())] + self.visit(ctx.lisExprTail()) if ctx.exp() else []
    def visitLisExprTail(self,ctx:MCParser.LisExprTailContext):
        return [self.visit(ctx.exp())] + self.visit(ctx.lisExprTail()) if ctx.exp() else []
'''
    def visitExp(self,ctx:MCParser.ExpContext):
        if (ctx.funcall()):
            return self.visit(ctx.funcall())
        else:
            return IntLiteral(int(ctx.INTLIT().getText()))
'''