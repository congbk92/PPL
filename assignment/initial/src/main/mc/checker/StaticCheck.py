
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
        cur_id_list = list(map(lambda x: x.name.name if type(x) is FuncDecl else x.variable, c))
        #print(cur_id_list)
        lstBlockIdx = [i for i in range(len(cur_id_list)) if cur_id_list[i] == "0_start_block"]
        startIdx = lstBlockIdx[-1]+1 if len(lstBlockIdx) else 0
        decl_cur_scope = cur_id_list[startIdx:]
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
        return reduce(lambda ac,it: ac + [self.visit(it,ac)], ast.decl, [VarDecl("0_start_block",VoidType())])

    def visitFuncDecl(self,ast, c):
        if self.isDuplicateId(c, ast.name.name):
            raise Redeclared(Function(), ast.name.name)
        try:
            local = reduce(lambda ac,it: ac + [self.visit(it,ac)] , ast.param, [])
        except Redeclared as e:
            raise Redeclared(Parameter(),e.n)
        cur_ast = FuncDecl(ast.name, ast.param, ast.returnType, Block([]))
        self.visitListNode(ast.body.member, c + [cur_ast] + [VarDecl("0_start_block",VoidType())] + local)
        return cur_ast

    def visitVarDecl(self, ast, c):
        if self.isDuplicateId(c,ast.variable):
            raise Redeclared(Variable(),ast.variable)
        return ast

    def visitBlock(self, ast, c):
        self.visitListNode(ast.member, c + [VarDecl("0_start_block",VoidType())])

    def visitId(self, ast, c):
        if ast.name not in c:
            raise Undeclared(Variable(),ast.name)
