import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_exp(self):
        input = """true && false"""
        expect = str(Binary('&&',BoolLit(True),BoolLit(False)))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,300))