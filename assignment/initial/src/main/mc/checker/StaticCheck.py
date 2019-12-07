
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
        name:str
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

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
    '''

    global_envi = [
    Symbol('0_start_block', None),
    Symbol("getInt",        MType([],               IntType())),
    Symbol("putInt",        MType([IntType()],      VoidType())), 
    Symbol("putIntLn",      MType([IntType()],      VoidType())),
    Symbol("getFloat",      MType([],               FloatType())),
    Symbol("putFloat",      MType([FloatType()],    VoidType())),
    Symbol("putFloatLn",    MType([FloatType()],    VoidType())),
    Symbol("putBool",       MType([BoolType()],     VoidType())),
    Symbol("putBoolLn",     MType([BoolType()],     VoidType())),
    Symbol("putString",     MType([StringType()],   VoidType())),
    Symbol("putStringLn",   MType([StringType()],   VoidType())),
    Symbol("putLn",         MType([],               VoidType())),
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

    def getLstIdCurScope(self,c):
        lst_block_idx = [i for i in range(len(c)) if c[i].name == "0_start_block"]
        return [x.name for x in c[lst_block_idx[-1]:]]

    def visitListLocalNode(self,ast, c):
        ac = c[:]
        for node in ast:
            new_symbol = self.visit(node,ac)
            if type(node) is VarDecl:
                ac = ac + [new_symbol]

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        #get all global variable and func decl
        c = reduce(lambda ac,it: ac + [self.visit(it,ac)], ast.decl, [Symbol('0_initial', None)] + StaticChecker.global_envi)
        
        #Check entry-point
        if 'main' not in [sym.name for sym in filter(lambda x: type(x.mtype) is MType, c)]:
            raise NoEntryPoint()

        del c[0]
        list(map(lambda node: self.visit(node,c), list(filter(lambda x: type(x) is FuncDecl,  ast.decl))))
        #self.visitListLocalNode(ast.decl, c)

    def visitFuncDecl(self,ast, c):
        if c[0].name is '0_initial':
            if ast.name.name in self.getLstIdCurScope(c): 
                raise Redeclared(Function(), ast.name.name)
            return Symbol(ast.name.name,MType([var.varType for var in ast.param], ast.returnType))
        else:
            try:
                cur_decl = reduce(lambda ac,it: ac + [self.visit(it,ac)] , ast.param, c + [Symbol('0_start_block', None)])
            except Redeclared as e:
                raise Redeclared(Parameter(),e.n)
            self.visitListLocalNode(ast.body.member, cur_decl)

    def visitVarDecl(self, ast, c):
        if ast.variable in self.getLstIdCurScope(c):
            raise Redeclared(Variable(),ast.variable)
        #print(ast.variable,ast.varType)
        return Symbol(ast.variable,ast.varType)

    def visitBlock(self, ast, c):
        self.visitListLocalNode(ast.member, c + [Symbol('0_start_block', None)])

    def visitId(self, ast, c):
        if ast.name not in [x.name for x in c]:
            raise Undeclared(Variable(),ast.name)
        #Return type of last element
        for i in reversed(c):
            if i.name == ast.name:
                #print('got')
                return i.mtype

    def visitCallExpr(self, ast, c):
        pass
    def visitUnaryOp(self, ast, c):
        pass
    def visitBinaryOp(self, ast, c):
        left_type = self.visit(ast.left, c)
        right_type = self.visit(ast.right, c)
        #print(ast.left, left_type)
        #print(ast.op)
        #print(ast.right, right_type)
        if ast.op is '=':
            validTypeOperand = [IntType, FloatType, BoolType, StringType]
            if (type(left_type) not in validTypeOperand) or (type(right_type) not in validTypeOperand):
                raise TypeMismatchInExpression(ast)
                #pass
            elif not isinstance(ast.left, LHS):
                raise NotLeftValue(ast.left)
            elif type(left_type) is FloatType:
                if type(right_type) is FloatType or type(right_type) is IntType:
                    return left_type
            elif type(left_type) is type(right_type):
                    return left_type
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op is '+':
            return left_type

        
    def visitArrayCell(self, ast, c):

        pass

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
    def visitIntLiteral(self, ast, c):
        return IntType()
    def visitFloatLiteral(self, ast, c):
        return FloatType()
    def visitStringLiteral(self, ast, c):
        return StringType()
    def visitBooleanLiteral(self, ast, c):
        return BoolType()