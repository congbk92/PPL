import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    '''
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """int main() {foo();}"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """int main () {
            putIntLn();
        }"""
        expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """int main () {
            putIntLn(getInt(4));
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([
            CallExpr(Id("foo"),[])]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    CallExpr(Id("putIntLn"),[
                        CallExpr(Id("getInt"),[IntLiteral(4)])
                        ])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_diff_numofparam_stmt_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    CallExpr(Id("putIntLn"),[])]))])
        expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,405))
    '''

    def test_simple(self):
        """More complex program"""
        input = Program([FuncDecl(Id("func"),[],VoidType(),Block([])),VarDecl("a",IntType())])
        expect = str(['func','a'])
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclare_variable(self):
        """More complex program"""
        input = Program([FuncDecl(Id("func"),[],VoidType(),Block([])),VarDecl("a",IntType()),VarDecl("func",IntType())])
        expect = "Redeclared Variable: func"
        self.assertTrue(TestChecker.test(input,expect,401))
    def test_redeclare_func(self):
        """More complex program"""
        input = Program([FuncDecl(Id("func"),[],VoidType(),Block([])),VarDecl("a",IntType()),FuncDecl(Id("a"),[],VoidType(),Block([]))])
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_redeclared_var_in_params(self):
        """Simple program: int main() {} """
        input = """int main(int a, boolean a){
                    boolean c;
                }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_redeclared_var_param_local_var(self):
        """Simple program: int main() {} """
        input = """int main(int a, boolean b){
                    boolean a;
                }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_redeclared_var_param_local_var_complex(self):
        """Simple program: int main() {} """
        input = """int main(int a, boolean b){
                    
                    int c;
                    {
                        boolean a;
                        {
                            int b;
                            {
                                string c;
                                float c;
                            }
                        }
                    }
                }"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_redeclared_var_param_local_var_complex_2(self):
        """Simple program: int main() {} """
        input = """int main(int a, boolean b){
                    {
                        boolean a;
                        {
                            int b;
                            {
                                string c;
                                float c;
                            }
                        }
                    }
                }"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,406))