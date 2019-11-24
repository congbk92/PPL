import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    
    def test_func_global_var_decl(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([
            CallExpr(Id("foo"),[])])),VarDecl("a",IntType())])
        expect = str(["main","a"])
        self.assertTrue(TestChecker.test(input,expect,403))
    
    def test_var_redecl(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("b"),[],IntType(),Block([
            CallExpr(Id("foo"),[])])),VarDecl("b",IntType())])
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_func_redecl(self):
        """Simple program: int main() {} """
        input = Program([VarDecl("a",IntType()),FuncDecl(Id("a"),[],IntType(),Block([
            CallExpr(Id("foo"),[])]))])
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_param_redecl(self):
        """Simple program: int main() {} """
        input = Program([VarDecl("a",IntType()),FuncDecl(Id("c"),[VarDecl("b",IntType()),VarDecl("b",IntType())],IntType(),Block([
            CallExpr(Id("foo"),[])]))])
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_local_var_redecl_param(self):
        """Simple program: int main() {} """
        input = Program([VarDecl("a",IntType()),FuncDecl(Id("b"),[VarDecl("c",IntType()),VarDecl("d",IntType())],IntType(),Block([
            VarDecl("a",IntType()),VarDecl("d",IntType())]))])
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_local_var_redecl(self):
        """Simple program: int main() {} """
        input = Program([VarDecl("a",IntType()),FuncDecl(Id("b"),[VarDecl("c",IntType()),VarDecl("d",IntType())],IntType(),Block([
            Block([VarDecl("a",IntType()),VarDecl("e",IntType()),
                VarDecl("f",IntType()),VarDecl("f",IntType())])]))])
        expect = "Redeclared Variable: f"
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_local_var_undecl_simple(self):
        """Simple program: int main() {} """
        input = Program([VarDecl("a",IntType()),FuncDecl(Id("b"),[VarDecl("c",IntType()),VarDecl("d",IntType())],IntType(),Block([
            Block([VarDecl("a",IntType()),VarDecl("e",IntType()),
                VarDecl("f",IntType()),Id("m")])]))])
        expect = "Undeclared Variable: m"
        self.assertTrue(TestChecker.test(input,expect,409))
    def test_local_var_undecl_complex(self):
        """Simple program: int main() {} """
        input = Program([VarDecl("a",IntType()),FuncDecl(Id("b"),[VarDecl("c",IntType()),VarDecl("d",IntType())],IntType(),Block([
            Block([VarDecl("a",IntType()),VarDecl("e",IntType()),
                VarDecl("f",IntType()),Id("a"),Id("b"),Id("c"),Id("d"),Id("e"),Id("f"),Id("i")])]))])
        expect = "Undeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,410))