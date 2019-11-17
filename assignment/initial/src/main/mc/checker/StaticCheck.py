
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
        return reduce(lambda ac, it: ac + [self.visit(it,ac)] if self.visit(it,ac) is not None else ac, ast.decl, [])

    def visitFuncDecl(self,ast, c):
        if ast.name.name in c:
            raise Redeclared(Function(), ast.name.name)
        else:
            c.extend([ast.name.name, '0_start_block']) # name of func and symbol to start block
            c = reduce(lambda ac, it: ac + [self.visit(it,ac)], ast.param, c)
            c.append('0_start_body_func')
            self.visit(ast.body,c)
    
    def visitVarDecl(self,ast, c):
        #Get list of index start block
        list_start_block_idx = [i for i in range(len(c)) if c[i] == '0_start_block']
        list_decl_in_cur_scope = c if len(list_start_block_idx) == 0 else c[len(list_start_block_idx)+1:]
        if ast.variable in list_decl_in_cur_scope:
            raise Redeclared(Variable(), ast.variable)
        else:
            return ast.variable

    def visitBlock(self,ast, c):
        if c[-1] != '0_start_body_func':
            c.append('0_start_block')
        else:
            c.pop()
        reduce(lambda ac, it: ac + [self.visit(it,ac)], ast.member, c)
        list_start_block_idx = [i for i in range(len(c)) if c[i] == '0_start_block']
        del c[list_start_block_idx[-1]:]   #delete all declare in current scope when out of it


