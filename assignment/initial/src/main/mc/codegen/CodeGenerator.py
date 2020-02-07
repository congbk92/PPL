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
        return [
                    Symbol("getInt",        MType([],               IntType()), CName(self.libName)),
                    Symbol("putInt",        MType([IntType()],      VoidType()), CName(self.libName)), 
                    Symbol("putIntLn",      MType([IntType()],      VoidType()), CName(self.libName)),
                    Symbol("getFloat",      MType([],               FloatType()), CName(self.libName)),
                    Symbol("putFloat",      MType([FloatType()],    VoidType()), CName(self.libName)),
                    Symbol("putFloatLn",    MType([FloatType()],    VoidType()), CName(self.libName)),
                    Symbol("putBool",       MType([BoolType()],     VoidType()), CName(self.libName)),
                    Symbol("putBoolLn",     MType([BoolType()],     VoidType()), CName(self.libName)),
                    Symbol("putString",     MType([StringType()],   VoidType()), CName(self.libName)),
                    Symbol("putStringLn",   MType([StringType()],   VoidType()), CName(self.libName)),
                    Symbol("putLn",         MType([],               VoidType()), CName(self.libName)),

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
        #Symbol("getInt", MType(list(), IntType()), CName(self.libName))
        #

        nenv = []
        for decl in ast.decl:
            if type(decl) is FuncDecl:
                sym = Symbol(decl.name.name, MType([param.varType for param in decl.param], decl.returnType), CName(self.className))
                nenv += [sym]
            else:
                sym = Symbol(decl.variable, decl.varType, Index(-1))
                nenv += [sym]
        # generate field derective
        lst_global_val_decl = [x for x in ast.decl if type(x) is VarDecl]
        for decl in lst_global_val_decl:
            self.emit.printout(self.emit.emitSTATICFIELD(decl.variable, decl.varType))

        e = SubBody(None, self.env + nenv)
        [self.visit(x, e) for x in ast.decl if type(x) is FuncDecl]
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list())), nenv, Frame("<init>", VoidType))
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
        #Print .var
        for member in body.member:
            if type(member) is VarDecl:
                new_idx = frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(new_idx, member.variable, member.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
                env += [Symbol(member.variable, member.varType, Index(new_idx))]

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        elif isMain:
            glbEnv = [sym for sym in env if sym.value.value == -1]
            for sym in glbEnv:
                if type(sym.mtype) is StringType:
                    self.emit.printout(self.emit.emitPUSHCONST("", StringType(), frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + sym.name, sym.mtype, frame))
                if type(sym.mtype) is ArrayType:
                    self.emit.printout(self.emit.emitARRAY(sym.mtype.eleType , sym.mtype.dimen, frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + sym.name, sym.mtype, frame))

        for x in body.member:
            result = self.visit(x,SubBody(frame, env))
            if result is not None:
                self.emit.printout(result[0])

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();
    
    def visitBlock(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        env = ctxt.sym
        frame.enterScope(False)
        #Print .var
        for member in ast.member:
            if type(member) is VarDecl:
                new_idx = frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(new_idx, member.variable, member.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
                env += [Symbol(member.variable, member.varType, Index(new_idx))]
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        for x in ast.member:
            result = self.visit(x,SubBody(frame, env))
            if result is not None:
                self.emit.printout(result[0])
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, [Symbol("0_return", MType([param.varType for param in ast.param], ast.returnType), CName(self.className))] + subctxt.sym, frame)

    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype
        #print(ast.param)
        #in_ = ("", list())
        code = ""
        for x in zip(ast.param,sym.mtype.partype):
            #print(self.visit(x, Access(frame, nenv, False, True)))
            str1, typ1 = self.visit(x[0], Access(frame, nenv, False, True))
            code += str1
            if type(typ1) is IntType and type(x[1]) is FloatType:
                code += self.emit.emitI2F(frame)
            #in_ = (in_[0] + str1, in_[1].append(typ1))
        #self.emit.printout(in_[0])
        code += self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame)
        return code, sym.mtype.rettype

    def visitVarDecl(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        if type(ast.varType) is ArrayType:
            sym = self.lookup(ast.variable, nenv, lambda x: x.name)
            self.emit.printout(self.emit.emitARRAY(ast.varType.eleType , ast.varType.dimen, frame))
            self.emit.printout(self.emit.emitWRITEVAR(ast.variable, ast.varType, sym.value.value, frame))
        #return SubBody(frame, nenv)

    def visitReturn(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = nenv[0]
        return_type = VoidType()
        if ast.expr is not None:
            code,return_type = self.visit(ast.expr, Access(frame, nenv, False, True))
            if type(return_type) is IntType and type(sym.mtype.rettype)  is FloatType:
                code += self.emit.emitI2F(frame)
                return_type = FloatType()
            self.emit.printout(code)
        self.emit.printout(self.emit.emitRETURN(return_type, frame))

    def visitId(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst

        sym = self.lookup(ast.name, nenv, lambda x: x.name)
        if sym.value.value == -1:
            #Global variable
            '''
            if type(sym.mtype) in [ArrayType, ArrayPointerType]:
                return self.emit.emitGETSTATIC(self.className + "." + ast.name, sym.mtype, frame), sym.mtype
            else:
            '''
            if not isLeft and isFirst:
                return self.emit.emitGETSTATIC(self.className + "." + ast.name, sym.mtype, frame), sym.mtype
            elif isLeft and  isFirst:
                return "", sym.mtype
            elif isLeft and not isFirst:
                return self.emit.emitPUTSTATIC(self.className + "." + ast.name, sym.mtype, frame), sym.mtype
        else:
            #local variable
            #if type(sym.mtype) in [ArrayType, ArrayPointerType]:
                #return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value , frame), sym.mtype
            #else:
            if not isLeft and isFirst:
                return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value , frame), sym.mtype
            elif isLeft and  isFirst:
                return "", sym.mtype
            elif isLeft and not isFirst:
                return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value , frame), sym.mtype

    def visitArrayCell(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst

        arr_code,arr_type = self.visit(ast.arr, Access(frame, nenv, False, True))
        idx_code,idx_type = self.visit(ast.idx, Access(frame, nenv, False, True))

        if isLeft:
            if isFirst:
                return arr_code + idx_code , arr_type.eleType
            else:
                return self.emit.emitASTORE(arr_type.eleType , frame) , arr_type.eleType
        else:
            return arr_code + idx_code + self.emit.emitALOAD(arr_type.eleType , frame), arr_type.eleType

    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        if ast.op == "=":
            #(self, frame, sym, isLeft, isFirst)
            lcode_first,ltype = self.visit(ast.left, Access(frame, nenv, True, True))
            rcode,rtype = self.visit(ast.right, Access(frame, nenv, False, True))
            if type(rtype) is IntType and type(ltype) is FloatType:
                rcode += self.emit.emitI2F(frame)
            lcode_second,ltype = self.visit(ast.left, Access(frame, nenv, True, False))
            return lcode_first + rcode + lcode_second, ltype

        elif ast.op in ["+", "-", "*", "/"]:
            returnType = IntType()
            lcode,ltype = self.visit(ast.left,o)
            rcode,rtype = self.visit(ast.right,o)
            if FloatType in [type(ltype),type(rtype)]:
                returnType = FloatType()
            
            if type(ltype) is IntType and type(returnType) is FloatType:
                lcode += self.emit.emitI2F(frame)
            if type(rtype) is IntType and type(returnType) is FloatType:
                rcode += self.emit.emitI2F(frame)

            if ast.op in ["+", "-"]:
                opcode = self.emit.emitADDOP(ast.op, returnType, frame)
            elif ast.op in ["*", "/"]:
                opcode = self.emit.emitMULOP(ast.op, returnType, frame)
            return lcode + rcode + opcode, returnType

        elif ast.op in ["&&", "||"]:
            lcode,ltype = self.visit(ast.left,o)
            rcode,rtype = self.visit(ast.right,o)
            new_label = frame.getNewLabel()
            if ast.op == '||':
                opcode =  self.emit.emitOROP(frame)
                short_circuit = self.emit.emitDUP(frame) + self.emit.emitIFTRUE(new_label,frame)
            else:
                opcode = self.emit.emitANDOP(frame)
                short_circuit = self.emit.emitDUP(frame) + self.emit.emitIFFALSE(new_label,frame)
            end_lable = self.emit.emitLABEL(new_label, frame)
            return lcode + short_circuit + rcode + opcode + end_lable, BoolType()
        elif ast.op in [">","<", "<=", ">=", "==", "!="]:
            lcode,ltype = self.visit(ast.left,o)
            rcode,rtype = self.visit(ast.right,o)
            if FloatType in [type(ltype), type(rtype)]:
                if type(ltype) is IntType:
                    lcode += self.emit.emitI2F(frame)
                if type(rtype) is IntType:
                    rcode += self.emit.emitI2F(frame)
                opcode = self.emit.emitFREOP(ast.op, frame)
            else:
                opcode = self.emit.emitREOP(ast.op, BoolType() ,  frame)
            return lcode + rcode + opcode , BoolType()
        elif ast.op == "%":
            lcode,ltype = self.visit(ast.left,o)
            rcode,rtype = self.visit(ast.right,o)
            opcode = self.emit.emitMOD(frame)
            return lcode + rcode + opcode , IntType()

    def visitUnaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        bdy_code,bdy_type = self.visit(ast.body,o)
        if ast.op == "!":
            opcode = self.emit.emitNOT(bdy_type, frame)
        if ast.op == "-":
            opcode = self.emit.emitNEGOP(bdy_type, frame)

        return bdy_code + opcode , bdy_type

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitStringLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value , StringType() , frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        value = "true" if ast.value else "false"
        return self.emit.emitPUSHICONST(value , frame), BoolType()