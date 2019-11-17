import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_exp(self):
        input = """true && false || false"""
        expect = str(Binary('||',Binary('&&',BoolLit(True),BoolLit(False)),BoolLit(False)))
        #expect = str(Binary('&&',Binary('||',BoolLit(False),BoolLit(False)),BoolLit(True)))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,300))