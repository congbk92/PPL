import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],VoidType(),Block([
                CallExpr(Id("putInt"),[IntLiteral(5)])]))])
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_float_ast(self):
        input = Program([
            FuncDecl(Id("main"),[],VoidType(),Block([
                CallExpr(Id("putFloatLn"),[FloatLiteral(1.1)])]))])
        expect = "1.1\n"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_int_vs_int(self):
        input = Program([
            FuncDecl(Id("main"),[],VoidType(),Block([
                CallExpr(Id("putInt"),[BinaryOp("+",IntLiteral(5),IntLiteral(5))])]))])
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_float_vs_float(self):
        input = Program([
            FuncDecl(Id("main"),[],VoidType(),Block([
                CallExpr(Id("putFloatLn"),[BinaryOp("+",FloatLiteral(1.1),FloatLiteral(1.1))])]))])
        expect = "2.2\n"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_float_vs_int(self):
        input = Program([
            FuncDecl(Id("main"),[],VoidType(),Block([
                CallExpr(Id("putFloatLn"),[BinaryOp("+",FloatLiteral(2.2),IntLiteral(2))])]))])
        expect = "4.2\n"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_int_vs_float(self):
        input = Program([
            FuncDecl(Id("main"),[],VoidType(),Block([
                CallExpr(Id("putFloatLn"),[BinaryOp("+",IntLiteral(4),FloatLiteral(4.1))])]))])
        expect = "8.1\n"
        self.assertTrue(TestCodeGen.test(input,expect,506))