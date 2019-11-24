
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast
        #self.count = 0

 
    
    def isDuplicateId(self,c,cur_id):
        var_func_decl_list = list(filter(lambda x: type(x) in (FuncDecl,VarDecl,Id), c))
        cur_id_list = list(map(lambda x: x.name.name if type(x) is FuncDecl else x.variable if type(x) is VarDecl else x.name, var_func_decl_list))
        lstBlockIdx = [i for i in range(len(cur_id_list)) if cur_id_list[i] == "0_start_block"]
        #print(cur_id_list)
        #print(lstBlockIdx)
        decl_cur_scope = cur_id_list[lstBlockIdx[-1]:]
        if cur_id in decl_cur_scope:
            return True
        else:
            return False

    def visitListNode(self,ast, c):
        ac = c[:]
        for node in ast:
            new_id = self.visit(node,ac)
            if new_id is not None:
                ac = ac + [new_id]

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        #TO DO: add built-in function to c
        '''
        int getInt(): reads and returns an integer value from the standard input
        void putInt(int i): prints the value of the integer i to the standard output
        void putIntLn(int i): same as putInt except that it also prints a newline
        float getFloat(): reads and returns a floating-point value from the standard input
        void putFloat(float f ): prints the value of the float f to the standard output
        void putFloatLn(float f ): same as putFloat except that it also prints a newline
        void putBool(boolean b): prints the value of the boolean b to the standard output
        void putBoolLn(boolean b): same as putBoolLn except that it also prints a new line
        void putString(string s): prints the value of the string to the standard output
        void putStringLn(string s): same as putStringLn except that it also prints a new line
        void putLn(): prints a newline to the standard output
        FuncDecl(Id("func"),[VarDecl("a",IntType())],ArrayPointerType(IntType()),Block([])),
        '''

        c = [Id("0_start_block"),
            FuncDecl(Id("getInt"),[],IntType(),Block([])),
            FuncDecl(Id("putInt"),[VarDecl("i",IntType())],VoidType(),Block([])),
            FuncDecl(Id("putIntLn"),[VarDecl("i",IntType())],VoidType(),Block([])),
            FuncDecl(Id("getFloat"),[],FloatType(),Block([])),
            FuncDecl(Id("putFloat"),[VarDecl("f",FloatType())],VoidType(),Block([])),
            FuncDecl(Id("putFloatLn"),[VarDecl("f",FloatType())],VoidType(),Block([])),
            FuncDecl(Id("putBool"),[VarDecl("b",BoolType())],VoidType(),Block([])),
            FuncDecl(Id("putBoolLn"),[VarDecl("b",BoolType())],VoidType(),Block([])),
            FuncDecl(Id("putString"),[VarDecl("s",StringType())],VoidType(),Block([])),
            FuncDecl(Id("putStringLn"),[VarDecl("s",StringType())],VoidType(),Block([])),
            FuncDecl(Id("putLn"),[],VoidType(),Block([]))]

        reduce(lambda ac,it: ac + [self.visit(it,ac)], ast.decl, c)

    def visitFuncDecl(self,ast, c):
        if self.isDuplicateId(c, ast.name.name):
            raise Redeclared(Function(), ast.name.name)
        
        cur_ast = FuncDecl(ast.name, ast.param, ast.returnType, Block([]))
        try:
            cur_decl = reduce(lambda ac,it: ac + [self.visit(it,ac)] , ast.param, c + [cur_ast] + [Id("0_start_block")])
        except Redeclared as e:
            raise Redeclared(Parameter(),e.n)
        self.visitListNode(ast.body.member, cur_decl)
        return cur_ast

    def visitVarDecl(self, ast, c):
        if self.isDuplicateId(c,ast.variable):
            raise Redeclared(Variable(),ast.variable)
        return ast

    def visitBlock(self, ast, c):
        self.visitListNode(ast.member, c + [Id("0_start_block")])

    def visitId(self, ast, c):
        if ast.name not in c:
            raise Undeclared(Variable(),ast.name)
    def visitDowhile(self, ast, c):
        pass
    def visitReturn(self, ast, c):
        pass
    def visitContinue(self, ast, c):
        pass
    def visitBreak(self, ast, c):
        pass
    def visitFor(self, ast, c):
        pass
    def visitIf(self, ast, c):
        pass
    def visitCallExpr(self, ast, c):
        pass
    def visitUnaryOp(self, ast, c):
        pass
    def visitBinaryOp(self, ast, c):
        pass
    def visitArrayCell(self, ast, c):
        pass