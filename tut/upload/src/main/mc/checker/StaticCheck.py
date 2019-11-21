
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

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        return reduce(lambda ac,it: ac + [self.visit(it,ac)], ast.decl, [])

    def visitFuncDecl(self,ast, c):
        if ast.name.name in c:
            raise Redeclared(Function(), ast.name.name)
        try:
            local = reduce(lambda ac,it: ac + [self.visit(it,ac)] , ast.param, [])
        except Redeclared as e:
            raise Redeclared(Parameter(),e.n)       
        ac = c + [ast.name.name] + ["0_start_block"] + local
        for node in ast.body.member:
            new_id = self.visit(node,ac)
            if new_id is not None:
                ac = ac + [new_id]
        return ast.name.name

    def visitVarDecl(self, ast, c):
        lstBlockIdx = [i for i in range(len(c)) if c[i] == "0_start_block"]
        startIdx = lstBlockIdx[-1]+1 if len(lstBlockIdx) else 0
        decl_cur_scope = c[startIdx:]
        if ast.variable in  decl_cur_scope:
            raise Redeclared(Variable(),ast.variable)
        return ast.variable
    def visitBlock(self, ast, c):
        tmp_c = c[:]
        tmp_c.append("0_start_block")
        reduce(lambda ac,it: ac + [self.visit(it,ac)] , ast.member, tmp_c)
    def visitId(self, ast, c):
        if ast.name not in c:
            raise Undeclared(Variable(),ast.name)

