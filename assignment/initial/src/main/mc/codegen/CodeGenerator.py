'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        for x in ast.decl:
            e = self.visit(x, e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list())), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        #isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        isMain = consdecl.name.name == "main"
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        #intype = [ArrayPointerType(StringType())] if isMain else list()
        intype = [ArrayPointerType(StringType())] if isMain else [param.varType  for param in consdecl.param]
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o
        env = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            for param in consdecl.param: 
                new_idx = frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(new_idx, param.variable, param.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
                env += [Symbol(param.variable, param.varType, Index(new_idx))] 

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            
        list(map(lambda x: self.visit(x, SubBody(frame, env)), body.member))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [Symbol(ast.name.name, MType([param.varType for param in ast.param], ast.returnType), CName(self.className))] + subctxt.sym)

    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype

        #in_ = ("", list())
        print(ast.param)
        for x in ast.param:
            #print(self.visit(x, Access(frame, nenv, False, True)))
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            self.emit.printout(str1)
            #in_ = (in_[0] + str1, in_[1].append(typ1))
        #self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))
        return "", sym.mtype.rettype
    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitVarDecl(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitId(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.name, nenv, lambda x: x.name)

        return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value , frame), sym.mtype

    def visitReturn(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        return_type = VoidType()
        if ast.expr is not None:
            code,return_type = self.visit(ast.expr, Access(frame, nenv, False, True))
            self.emit.printout(code)
        self.emit.printout(self.emit.emitRETURN(return_type, frame))

    def visitBinaryOp(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        returnType = IntType()

        lcode,ltype = self.visit(ast.left,o)
        rcode,rtype = self.visit(ast.right,o)
        if FloatType in [type(ltype),type(rtype)]:
            returnType = FloatType()
        
        if type(ltype) is IntType and type(returnType) is FloatType:
            lcode += self.emit.emitI2F(frame)
        if type(rtype) is IntType and type(returnType) is FloatType:
            rcode += self.emit.emitI2F(frame)

        opcode = ""
        if ast.op in ["+","-"]:
            opcode += self.emit.emitADDOP(ast.op, returnType, frame)
        elif ast.op in ["*","/"]:
            opcode += self.emit.emitMULOP(ast.op, returnType, frame)

        return lcode + rcode + opcode, returnType

