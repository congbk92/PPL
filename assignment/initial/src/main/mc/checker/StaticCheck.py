
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
        self.reachable_func = set()
        #self.count = 0

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
        
        lst_user_func = list(map(lambda node: node.name.name , list(filter(lambda x: type(x) is FuncDecl,  ast.decl))))
        #Check entry-point
        if 'main' not in lst_user_func:
            raise NoEntryPoint()

        del c[0]
        list(map(lambda node: self.visit(node,c), list(filter(lambda x: type(x) is FuncDecl,  ast.decl))))
        # Check unreachable func
        for func in lst_user_func:
            if func != 'main' and func not in self.reachable_func:
                raise UnreachableFunction(func)

    def isFullReturnStmt(self,stmt):
        if type(stmt) is Return:
            return True
        elif type(stmt) is If:
            if stmt.elseStmt is None:
                return False
            else:
                return self.isFullReturnStmt(stmt.thenStmt) & self.isFullReturnStmt(stmt.elseStmt)
        elif type(stmt) is Block:
            return reduce(lambda ac,it: ac | self.isFullReturnStmt(it) , stmt.member , False)
        else:
            return False

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
            self.visitListLocalNode(ast.body.member, cur_decl + [Symbol('0_return_type', ast.returnType)])
            #check not return
            if type(ast.returnType) is not VoidType and not self.isFullReturnStmt(ast.body):
                raise FunctionNotReturn(ast.name.name)

    def visitVarDecl(self, ast, c):
        if ast.variable in self.getLstIdCurScope(c):
            raise Redeclared(Variable(),ast.variable)
        #print(ast.variable,ast.varType)
        return Symbol(ast.variable,ast.varType)

    def visitBlock(self, ast, c):
        self.visitListLocalNode(ast.member, c + [Symbol('0_start_block', None)])

    def visitId(self, ast, c):
        if ast.name not in [x.name for x in c]:
            raise Undeclared(Identifier(),ast.name)
        #Return type of last element
        for i in reversed(c):
            if i.name == ast.name:
                #print('got')
                return i.mtype

    def getTypeAssign(self,lhs,rhs):
        primitive_type = [IntType, FloatType, BoolType, StringType]
        if type(lhs) in primitive_type and type(rhs) in primitive_type:
            if type(lhs) is type(rhs):
                return lhs
            elif type(lhs) is FloatType and type(rhs) is IntType:
                return lhs
        elif type(lhs) is ArrayPointerType and type(rhs) in [ArrayPointerType, ArrayType]:
            return lhs if type(lhs.eleType) is type(rhs.eleType) else None

    def visitBinaryOp(self, ast, c):
        left_type = self.visit(ast.left, c)
        right_type = self.visit(ast.right, c)
        #print(ast.left, left_type)
        #print(ast.op)
        #print(ast.right, right_type)
        if ast.op == '=':
            if not isinstance(ast.left, LHS) or not isinstance(left_type, Type):

            #if type(ast.left) not in [Id, ArrayCell]: 
                raise NotLeftValue(ast.left)
            validTypeOperand = [IntType, FloatType, BoolType, StringType]
            if (type(left_type) in validTypeOperand) and (type(right_type) in validTypeOperand):
                type_result = self.getTypeAssign(left_type, right_type)
                if type_result:
                    return type_result
        elif ast.op == '%':
            if type(left_type) is IntType and type(right_type) is IntType:
                return left_type
        elif ast.op in ['+', '-', '*', '/']:
            validTypeOperand = [IntType, FloatType]
            if (type(left_type) in validTypeOperand) and (type(right_type) in validTypeOperand):
                return FloatType() if FloatType in [type(left_type), type(right_type)] else IntType()
        elif ast.op in ['<', '<=', '>', '>=']:
            validTypeOperand = [IntType, FloatType]
            if (type(left_type) in validTypeOperand) and (type(right_type) in validTypeOperand):
                return BoolType()
        elif ast.op in ['==', '!=']:
            validTypeOperand = [IntType, BoolType]
            if (type(left_type) in validTypeOperand) and (type(right_type) in validTypeOperand):
                if type(left_type) is type(right_type):
                    return BoolType()
        elif ast.op in ['&&', '||']:
            if (type(left_type) is BoolType) and (type(right_type) is BoolType):
                return BoolType()

        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        if ast.method.name not in [x.name for x in c]:
            raise Undeclared(Function(), ast.method.name)
        for i in reversed(c):
            if i.name == ast.method.name:
                if len(i.mtype.partype) == len(ast.param):
                    type_param = [self.visit(x,c) for x in ast.param]
                    type_pass = [type(self.getTypeAssign(x[0],x[1])) for x in zip(i.mtype.partype, type_param)]
                    #print("i.mtype.partype = ")
                    #print (i.mtype.partype)
                    #print("type_param = ")
                    #print(type_param)
                    #print("type_pass = ")
                    #print(type_pass)
                    if type(None) not in type_pass:
                        self.reachable_func.add(i.name)
                        return i.mtype.rettype

        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        expr_type = self.visit(ast.body,c)
        if ast.op == '-':
            if type(expr_type) is IntType or type(expr_type) is FloatType:
                return expr_type
        elif ast.op == '!':
            if type(expr_type) is BoolType:
                return expr_type

        raise TypeMismatchInExpression(ast)

    def visitArrayCell(self, ast, c):
        arr_type = self.visit(ast.arr, c)
        idx_type = self.visit(ast.idx, c)
        if type(arr_type) is ArrayType or type(arr_type) is ArrayPointerType:
            if type(idx_type) is IntType:
                return arr_type.eleType
        raise TypeMismatchInExpression(ast)

    def visitDowhile(self, ast, c):
        # visit list stmt
        if type(self.visit(ast.exp, c)) is not BoolType:
            raise TypeMismatchInStatement(ast)
        [self.visit(stmt, c + [Symbol('0_in_loop', None)]) for stmt in ast.sl]

    def visitReturn(self, ast, c):
        for i in reversed(c):
            if i.name =='0_return_type':
                if type(i.mtype) is not VoidType and ast.expr is not None:
                    if self.getTypeAssign(i.mtype,self.visit(ast.expr,c)) is None:
                        raise TypeMismatchInStatement(ast)
                elif type(i.mtype) is VoidType and ast.expr is not None:
                    raise TypeMismatchInStatement(ast)
                elif type(i.mtype) is not VoidType and ast.expr is None:
                    raise TypeMismatchInStatement(ast) 
                break

    def visitContinue(self, ast, c):
        if '0_in_loop' not in [x.name for x in c]:
            raise ContinueNotInLoop()

    def visitBreak(self, ast, c):
        if '0_in_loop' not in [x.name for x in c]:
            raise BreakNotInLoop()

    def visitFor(self, ast, c):
        if [type(self.visit(ast.expr1,c)),type(self.visit(ast.expr2,c)),type(self.visit(ast.expr3,c))] != [IntType,BoolType,IntType]:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.loop, c + [Symbol('0_in_loop', None)])

    def visitIf(self, ast, c):
        if type(self.visit(ast.expr,c)) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt,c)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt,c)

    def visitIntLiteral(self, ast, c):
        return IntType()
    def visitFloatLiteral(self, ast, c):
        return FloatType()
    def visitStringLiteral(self, ast, c):
        return StringType()
    def visitBooleanLiteral(self, ast, c):
        return BoolType()