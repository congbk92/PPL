import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """int a,b
        			float c
        			int a[100]"""
        expect = str(Program([VarDecl(IntType(),'a'),VarDecl(IntType(),'b'),
        	VarDecl(FloatType(),'c'),VarDecl(ArrayType(IntType(),100),'a')]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

       