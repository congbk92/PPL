import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    # Test redeclare build-in func

    def test_redeclared_build_in_getInt_func(self):
        input = """ int[] getInt(int a, int b, int c, int d){}"""
        expect = "Redeclared Function: getInt"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_build_in_getInt_var(self):
        input = """int getInt;"""
        expect = "Redeclared Variable: getInt"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_build_in_putInt_func(self):
        input = """ int[] putInt(int a, int b, int c, int d){}"""
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_build_in_putInt_var(self):
        input = """int putInt;"""
        expect = "Redeclared Variable: putInt"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_build_in_putIntLn_func(self):
        input = """ int[] putIntLn(int a, int b, int c, int d){}"""
        expect = "Redeclared Function: putIntLn"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_build_in_putIntLn_var(self):
        input = """int putIntLn;"""
        expect = "Redeclared Variable: putIntLn"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_build_in_getFloat_func(self):
        input = """ int[] getFloat(int a, int b, int c, int d){}"""
        expect = "Redeclared Function: getFloat"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_build_in_getFloat_var(self):
        input = """int getFloat;"""
        expect = "Redeclared Variable: getFloat"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_build_in_putFloat_func(self):
        input = """ int[] putFloat(int a, int b, int c, int d){}"""
        expect = "Redeclared Function: putFloat"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_build_in_putFloat_var(self):
        input = """int putFloat;"""
        expect = "Redeclared Variable: putFloat"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_build_in_putFloatLn_func(self):
        input = """ int[] putFloatLn(int a, int b, int c, int d){}"""
        expect = "Redeclared Function: putFloatLn"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_build_in_putFloatLn_var(self):
        input = """int putFloatLn;"""
        expect = "Redeclared Variable: putFloatLn"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_build_in_putBool_func(self):
        input = """ int[] putBool(int a, int b, int c, int d){}"""
        expect = "Redeclared Function: putBool"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_build_in_putBool_var(self):
        input = """int putBool;"""
        expect = "Redeclared Variable: putBool"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_build_in_putBoolLn_func(self):
        input = """ int[] putBoolLn(int a, int b, int c, int d){}"""
        expect = "Redeclared Function: putBoolLn"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_build_in_putBoolLn_var(self):
        input = """int putBoolLn;"""
        expect = "Redeclared Variable: putBoolLn"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_build_in_putString_func(self):
        input = """ int[] putString(int a, int b, int c, int d){}"""
        expect = "Redeclared Function: putString"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_build_in_putString_var(self):
        input = """int putString;"""
        expect = "Redeclared Variable: putString"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_build_in_putStringLn_func(self):
        input = """ int[] putStringLn(int a, int b, int c, int d){}"""
        expect = "Redeclared Function: putStringLn"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_build_in_putStringLn_var(self):
        input = """int putStringLn;"""
        expect = "Redeclared Variable: putStringLn"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_build_in_putLn_func(self):
        input = """ int[] putLn(int a, int b, int c, int d){}"""
        expect = "Redeclared Function: putLn"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_build_in_putLn_var(self):
        input = """int putLn;"""
        expect = "Redeclared Variable: putLn"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_build_in_param(self):
        input = """int main(string getInt, string putInt, string putIntLn, string getFloat, string putFloat, string putFloatLn, 
        string putBool, string putBoolLn, string putString, string putStringLn, string putLn, int abc){
            int abc;
        }"""
        expect = "Redeclared Variable: abc"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_build_in_local_var(self):
        input = """int main(int abc1){
            string getInt, putInt, putIntLn, getFloat, putFloat, putFloatLn, putBool, putBoolLn, putString, putStringLn, putLn;
            int abc1;
        }"""
        expect = "Redeclared Variable: abc1"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_var_main(self):
        input = """int main(int abc1){
            string getInt, putInt, putIntLn, getFloat, putFloat, putFloatLn, putBool, putBoolLn, putString, putStringLn, putLn;
        }
        int main;
        """
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_func_main(self):
        input = """int main(int abc1){
            string getInt, putInt, putIntLn, getFloat, putFloat, putFloatLn, putBool, putBoolLn, putString, putStringLn, putLn;
        }
        int main(){}
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,400))

    #Test redeclare parameter, variable, user-define function
    def test_redeclare_func_with_func(self):
        input = """int func(){}
                void func(){}
        """
        expect = "Redeclared Function: func"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclare_func_with_var(self):
        input = """int func;
                void func(){}
        """
        expect = "Redeclared Function: func"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclare_global_var_with_func(self):
        input = """int var(){}
                int var;
        """
        expect = "Redeclared Variable: var"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclare_global_var_with_var(self):
        input = """int var;
                string var;
        """
        expect = "Redeclared Variable: var"
        self.assertTrue(TestChecker.test(input,expect,400))
    

    def test_redeclare_param_simple(self):
        input = """
                int func(){}
                string var;
                void main(int a, int b, string c, boolean d, float e, int c[]){}
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclare_param_complex(self):
        input = """
                int func(){}
                string var;
                void main(int a, int b, string c, boolean d, float e, float func, string var, boolean main, int e[]){}
        """
        expect = "Redeclared Parameter: e"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclare_local_var(self):
        input = """
                int func(){}
                string var;
                void main(int a, int b, string c, boolean d, float e, float func, string var)
                {
                    int var_local;
                    string var_local;
                }
        """
        expect = "Redeclared Variable: var_local"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclare_local_var_with_param(self):
        input = """
                int func(){}
                string var;
                void main(int a, int b, string c, boolean d, float e, float func, string var, int param)
                {
                    int main;
                    int var_local;
                    string param;
                }
        """
        expect = "Redeclared Variable: param"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclare_local_var_more_complex(self):
        input = """
                int func(){}
                string var;
                void main(int a, int b, string c, boolean d, float e, float func, string var, int param, int main)
                {
                    {
                        string local_var[1000];
                        int a; int b; string c; boolean d; float e; float func; string var; int param; int main;
                        {
                            int a; int b; string c; boolean d; float e; float func; string var; int param; int main;
                            {
                                int a; int b; string c; boolean d; float e; float func; string var; int param; int main;
                            }
                            {
                                int a; int b; string c; boolean d; float e; float func; string var; int param; int main;
                            }
                            {
                                int a; int b; string c; boolean d; float e; float func; string var; int param; int main;
                                {
                                    int a; int b; string c; boolean d; float e; float func; string var; int param; int main;
                                }
                            }
                        }
                        boolean local_var;
                    }
                    float a[100];
                }
        """
        expect = "Redeclared Variable: local_var"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_no_entry_point_1(self):
        input = """
                int func(){}
                string var;
                void func2(int a, int b, string c, boolean d, float e, float func, string var)
                {
                    int main;
                    int var_local;
                }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_no_entry_point_2(self):
        input = """
                int func(){}
                string var;
                void func2(int a, int b, string c, boolean d, float e, float func, string var)
                {
                    int main;
                    int var_local;
                }
                int main;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_undeclare_Id(self):
        input = """
                int b;
                int main()
                {
                b;
                a;
                }
        """
        expect = "Undeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_undeclare_Id_complex(self):
        input = """
                int main()
                {
                    a;
                    b;
                }
                int a;
        """
        expect = "Undeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,400))
    #TO DO: add more
    def test_not_left_value_binary_op(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("e",IntType()),
           BinaryOp("=",Id('a'),BinaryOp("=",BinaryOp("+",Id('c'),Id('b')),BinaryOp("=",Id('e'),Id('d'))))]))])
        expect = "Not Left Value: BinaryOp(+,Id(c),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_float_lit(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",FloatType()),
           BinaryOp("=",FloatLiteral(1.3),Id('a'))]))])
        expect = "Not Left Value: FloatLiteral(1.3)"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_int_lit(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),
           BinaryOp("=",IntLiteral(3),Id('a'))]))])
        expect = "Not Left Value: IntLiteral(3)"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_bool_lit(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",BoolType()),
           BinaryOp("=",BooleanLiteral(True),Id('a'))]))])
        expect = "Not Left Value: BooleanLiteral(true)"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_string_lit(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",StringType()),
           BinaryOp("=",StringLiteral("This is a string"),Id('a'))]))])
        expect = "Not Left Value: StringLiteral(This is a string)"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_unary_not(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",BoolType()),
           BinaryOp("=",UnaryOp("!",Id("a")),Id('a'))]))])
        expect = "Not Left Value: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_unary_sub(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",FloatType()),
           BinaryOp("=",UnaryOp("-",Id("a")),Id('a'))]))])
        expect = "Not Left Value: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_call_expr(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",FloatType()),
           BinaryOp("=",CallExpr(Id("func"), []),Id('a'))])), 
        FuncDecl(Id("func"), [],VoidType(),Block([])) ])
        expect = "Not Left Value: CallExpr(Id(func),[])"
        self.assertTrue(TestChecker.test(input,expect,400))
    '''
    '''
    def test_not_left_value_func_name(self):
        """Simple program: int main() {} """
        input = """
                int[] func(int b[])
                {
                    return b;
                }
                void main()
                {
                    int a[100];
                    int b[100];
                    func = a;
                }
        """
        expect = "Not Left Value: Id(func)"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_assign_op_arr_vs_arr(self):
        """Simple program: int main() {} """
        input = """
                void main()
                {
                    int a[100];
                    int b[100];
                    a = b;
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_assign_op_arr_vs_arr_pnt(self):
        """Simple program: int main() {} """
        input = """
                int[] func(int b[])
                {
                    return b;
                }
                void main()
                {
                    int a[100];
                    int b[100];
                    a = func(b);
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(func),[Id(b)]))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_assign_operator_complex(self):
        """Simple program: int main() {} """
        input = """
                int main()
                {
                    int a1,a2;
                    a2 = 1;
                    a1 = a;

                    float b1,b2;
                    b2 = 1e5;
                    b1 = b2;
                    b1 = a1 = a2;

                    boolean c1,c2;
                    c2 = true;
                    c2= false;
                    c1 = c2;

                    string d1,d2;
                    d2 = "this is a string";
                    d1 = d2;

                    float c;
                    a = c = a = a1 = a2;
                }
                int a;
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(=,Id(c),BinaryOp(=,Id(a),BinaryOp(=,Id(a1),Id(a2)))))"
        self.assertTrue(TestChecker.test(input,expect,400))
