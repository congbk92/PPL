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
                int func()
                {
                    return 1;
                }
                string var;
                void main(int a, int b, string c, boolean d, float e, int c[]){}
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclare_param_complex(self):
        input = """
                int func()
                {
                    return 0;
                }
                string var;
                void main(int a, int b, string c, boolean d, float e, float func, string var, boolean main, int e[]){}
        """
        expect = "Redeclared Parameter: e"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclare_local_var(self):
        input = """
                int func()
                {
                    return 0;
                }
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
                int func()
                {
                    return 0;
                }
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
                int func()
                {
                    return 0;
                }
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
                int func()
                {
                    return 0;
                }
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
                int func()
                {
                    return 0;
                }
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
        expect = "Undeclared Identifier: a"
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
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,400))

    #TO DO: add more
    def test_not_left_value_binary_op(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("e",IntType()),
           BinaryOp("=",Id('a'),BinaryOp("=",BinaryOp("+",Id('c'),Id('b')),BinaryOp("=",Id('e'),Id('d'))))]))])
        expect = "Not Left Value: BinaryOp(+,Id(c),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_float_lit(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",FloatType()),
           BinaryOp("=",FloatLiteral(1.3),Id('a'))]))])
        expect = "Not Left Value: FloatLiteral(1.3)"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_int_lit(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),
           BinaryOp("=",IntLiteral(3),Id('a'))]))])
        expect = "Not Left Value: IntLiteral(3)"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_bool_lit(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",BoolType()),
           BinaryOp("=",BooleanLiteral(True),Id('a'))]))])
        expect = "Not Left Value: BooleanLiteral(true)"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_string_lit(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",StringType()),
           BinaryOp("=",StringLiteral("This is a string"),Id('a'))]))])
        expect = "Not Left Value: StringLiteral(This is a string)"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_unary_not(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",BoolType()),
           BinaryOp("=",UnaryOp("!",Id("a")),Id('a'))]))])
        expect = "Not Left Value: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_unary_sub(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",FloatType()),
           BinaryOp("=",UnaryOp("-",Id("a")),Id('a'))]))])
        expect = "Not Left Value: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_not_left_value_call_expr(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",FloatType()),
           BinaryOp("=",CallExpr(Id("func"), []),Id('a'))])), 
        FuncDecl(Id("func"), [],VoidType(),Block([])) ])
        expect = "Not Left Value: CallExpr(Id(func),[])"
        self.assertTrue(TestChecker.test(input,expect,400))
    '''
    '''
    def test_not_left_value_func_name(self):
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

    def test_assign_op_int_vs_arr(self):
        input = """
                string a,b;
                void main()
                {
                    int a;
                    int b[100];
                    a = b;
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_assign_int_vs_float(self):
        input = """
                int a,b;
                void main()
                {
                    int a;
                    float b;
                    a = b;
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_assign_int_vs_bool(self):
        input = """
                int a,b;
                void main()
                {
                    int a;
                    boolean b;
                    a = b;
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_assign_int_vs_string(self):
        input = """
                int a,b;
                void main()
                {
                    int a;
                    string b;
                    a = b;
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_assign_float_vs_bool(self):
        input = """
                int a,b;
                void main()
                {
                    float a;
                    boolean b;
                    a = b;
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_assign_float_vs_string(self):
        input = """
                int a,b;
                void main()
                {
                    float a;
                    string b;
                    a = b;
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_assign_bool_vs_string(self):
        input = """
                int a,b;
                void main()
                {
                    boolean a;
                    string b;
                    a = b;
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_or_int_vs_int(self):
        input = """
                boolean a,b;
                int main()
                {
                    int a,b;
                    a = a || b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_or_float_vs_float(self):
        input = """
                boolean a,b;
                int main()
                {
                    float a,b;
                    a = a || b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_or_string_vs_string(self):
        input = """
                boolean a,b;
                int main()
                {
                    string a,b;
                    a = a || b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_and_int_vs_int(self):
        input = """
                boolean a,b;
                int main()
                {
                    int a,b;
                    a = a && b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_and_float_vs_float(self):
        input = """
                boolean a,b;
                int main()
                {
                    float a,b;
                    a = a && b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_and_string_vs_string(self):
        input = """
                boolean a,b;
                int main()
                {
                    string a,b;
                    a = a && b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_equal_float_vs_float(self):
        input = """
                boolean a,b;
                int main()
                {
                    float a,b;
                    a == b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_equal_string_vs_string(self):
        input = """
                boolean a,b;
                int main()
                {
                    string a,b;
                    a == b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_equal_int_vs_bool(self):
        input = """
                boolean a,b;
                int main()
                {
                    int a;
                    boolean b;
                    a == b;
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_float_vs_float(self):
        input = """
                boolean a,b;
                int main()
                {
                    float a,b;
                    a != b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_string_vs_string(self):
        input = """
                boolean a,b;
                int main()
                {
                    string a,b;
                    a != b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_int_vs_bool(self):
        input = """
                boolean a,b;
                int main()
                {
                    int a;
                    boolean b;
                    a != b;
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_bigger_bool_vs_bool(self):
        input = """
                int a,b;
                int main()
                {
                    boolean a,b;
                    a > b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_bigger_string_vs_string(self):
        input = """
                int a,b;
                int main()
                {
                    string a,b;
                    a > b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_bigger_equal_bool_vs_bool(self):
        input = """
                int a,b;
                int main()
                {
                    boolean a,b;
                    a >= b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_bigger_equal_string_vs_string(self):
        input = """
                int a,b;
                int main()
                {
                    string a,b;
                    a >= b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_less_bool_vs_bool(self):
        input = """
                int a,b;
                int main()
                {
                    boolean a,b;
                    a < b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_less_string_vs_string(self):
        input = """
                int a,b;
                int main()
                {
                    string a,b;
                    a < b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_less_equal_bool_vs_bool(self):
        input = """
                int a,b;
                int main()
                {
                    boolean a,b;
                    a <= b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_less_equal_string_vs_string(self):
        input = """
                int a,b;
                int main()
                {
                    string a,b;
                    a <= b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_add_bool_vs_bool(self):
        input = """
                int a,b;
                int main()
                {
                    boolean a,b;
                    a + b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_add_string_vs_string(self):
        input = """
                int a,b;
                int main()
                {
                    string a,b;
                    a + b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_sub_bool_vs_bool(self):
        input = """
                int a,b;
                int main()
                {
                    boolean a,b;
                    a - b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_sub_string_vs_string(self):
        input = """
                int a,b;
                int main()
                {
                    string a,b;
                    a - b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_mul_bool_vs_bool(self):
        input = """
                int a,b;
                int main()
                {
                    boolean a,b;
                    a * b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_mul_string_vs_string(self):
        input = """
                int a,b;
                int main()
                {
                    string a,b;
                    a * b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_div_bool_vs_bool(self):
        input = """
                int a,b;
                int main()
                {
                    boolean a,b;
                    a / b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_div_string_vs_string(self):
        input = """
                int a,b;
                int main()
                {
                    string a,b;
                    a / b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_mod_bool_vs_bool(self):
        input = """
                int a,b;
                int main()
                {
                    boolean a,b;
                    a % b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_mod_string_vs_string(self):
        input = """
                int a,b;
                int main()
                {
                    string a,b;
                    a % b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_mod_float_vs_float(self):
        input = """
                int a,b;
                int main()
                {
                    float a,b;
                    a % b; 
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_int(self):
        input = """
                boolean a;
                int main()
                {
                    int a;
                    !a; 
                }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_float(self):
        input = """
                boolean a;
                int main()
                {
                    float a;
                    !a; 
                }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_string(self):
        input = """
                boolean a;
                int main()
                {
                    string a;
                    !a; 
                }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))


    def test_sub_unary_bool(self):
        input = """
                int a;
                int main()
                {
                    boolean a;
                    -a; 
                }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_sub_unary_string(self):
        input = """
                int a;
                int main()
                {
                    string a;
                    -a; 
                }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_arr_subcripting_by_string(self):
        input = """
                int a;
                int main()
                {
                    string a;
                    string b[100];
                    a = b[a]; 
                }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_arr_subcripting_by_float(self):
        input = """
                int a;
                int main()
                {
                    float a;
                    string b[100];
                    a = b[a]; 
                }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_arr_subcripting_by_bool(self):
        input = """
                int a;
                int main()
                {
                    boolean a;
                    string b[100];
                    a = b[a]; 
                }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_arr_subcripting_not_arr_string(self):
        input = """
                int a;
                int main()
                {
                    string b;
                    a = b[a]; 
                }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_arr_subcripting_not_arr_float(self):
        input = """
                int a;
                int main()
                {
                    float b;
                    a = b[a]; 
                }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_arr_subcripting_not_arr_bool(self):
        input = """
                int a;
                int main()
                {
                    boolean b;
                    a = b[a]; 
                }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_arr_subcripting_not_arr_int(self):
        input = """
                int a;
                int main()
                {
                    int b;
                    a = b[a]; 
                }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_arr_subcripting_not_int(self):
        input = """
                int a;
                int main()
                {
                    int b[100];
                    a = b[a * a - a/a%a];
                    a = b[1.1 + a * a - a/a%a]; 
                }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),BinaryOp(-,BinaryOp(+,FloatLiteral(1.1),BinaryOp(*,Id(a),Id(a))),BinaryOp(%,BinaryOp(/,Id(a),Id(a)),Id(a))))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_int_vs_float(self):
        input = """
                void func(int a){}
                int main()
                {
                    float b;
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_int_vs_bool(self):
        input = """
                void func(int a){}
                int main()
                {
                    boolean b;
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_int_vs_string(self):
        input = """
                void func(int a){}
                int main()
                {
                    string b;
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_int_vs_void(self):
        input = """
                void param(){}
                void func(int a){}
                int main()
                {
                    func(param); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(param)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_float_vs_bool(self):
        input = """
                void func(float a){}
                int main()
                {
                    boolean b;
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_float_vs_string(self):
        input = """
                void func(float a){}
                int main()
                {
                    string b;
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_float_vs_void(self):
        input = """
                void param(){}
                void func(float a){}
                int main()
                {
                    func(param); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(param)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_bool_vs_string(self):
        input = """
                void func(boolean a){}
                int main()
                {
                    string b;
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_bool_vs_void(self):
        input = """
                void param(){}
                void func(boolean a){}
                int main()
                {
                    func(param); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(param)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_string_vs_void(self):
        input = """
                void param(){}
                void func(string a){}
                int main()
                {
                    func(param); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(param)])"
        self.assertTrue(TestChecker.test(input,expect,400))


    def test_call_func_arr_int_vs_float(self):
        input = """
                void func(int a[]){}
                int main()
                {
                    float b[100];
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_arr_int_vs_bool(self):
        input = """
                void func(int a[]){}
                int main()
                {
                    boolean b[100];
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_arr_int_vs_string(self):
        input = """
                void func(int a[]){}
                int main()
                {
                    string b[100];
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_arr_float_vs_bool(self):
        input = """
                void func(float a[]){}
                int main()
                {
                    boolean b[100];
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_arr_float_vs_string(self):
        input = """
                void func(float a[]){}
                int main()
                {
                    string b[100];
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_arr_bool_vs_string(self):
        input = """
                void func(boolean a[]){}
                int main()
                {
                    string b[100];
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_arr_ptn_int_vs_float(self):
        input = """
                float[] b()
                {
                    float result[1];
                    return result;
                }
                void func(int a[]){}
                int main()
                {
                    func(b()); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[CallExpr(Id(b),[])])"
        self.assertTrue(TestChecker.test(input,expect,400))


    def test_call_func_arr_ptn_int_vs_float(self):
        input = """
                float[] b()
                {
                    float result[1];
                    return result;
                }
                void func(int a[]){}
                int main()
                {
                    func(b()); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[CallExpr(Id(b),[])])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_arr_ptn_int_vs_bool(self):
        input = """
                boolean[] b()
                {
                    boolean result[1];
                    return result;
                }
                void func(int a[]){}
                int main()
                {
                    func(b()); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[CallExpr(Id(b),[])])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_arr_ptn_int_vs_string(self):
        input = """
                string[] b()
                {
                    string result[1];
                    return result;
                }
                void func(int a[]){}
                int main()
                {
                    func(b()); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[CallExpr(Id(b),[])])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_arr_ptn_float_vs_bool(self):
        input = """
                boolean[] b()
                {
                    boolean result[1];
                    return result;
                }
                void func(float a[]){}
                int main()
                {
                    func(b()); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[CallExpr(Id(b),[])])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_arr_ptn_float_vs_string(self):
        input = """
                string[] b()
                {
                    string result[1];
                    return result;
                }
                void func(float a[]){}
                int main()
                {
                    func(b()); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[CallExpr(Id(b),[])])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_arr_ptn_bool_vs_string(self):
        input = """
                string[] b()
                {
                    string result[1];
                    return result;
                }
                void func(boolean a[]){}
                int main()
                {
                    func(b()); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[CallExpr(Id(b),[])])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_arr_by_func_type(self):
        input = """
                boolean[] b()
                {
                    boolean result[1];
                    return result;
                }
                void func(boolean a[]){}
                int main()
                {
                    func(b); 
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_more_num_param(self):
        input = """
                boolean[] b()
                {
                    boolean result[1];
                    return result;
                }
                void func(boolean a[]){}
                int main()
                {
                    func(b(1));
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(b),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_less_num_param(self):
        input = """
                boolean[] b(int a)
                {
                    boolean result[1];
                    return result;
                }
                void func(boolean a[]){}
                int main()
                {
                    func(b());
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(b),[])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_operator_complex(self):
        input = """
                void        func_void(){}
                int         func_int(){return 1;}
                float       func_float(){return 1;}
                boolean     func_boolean(){return true;}
                string      func_string(){return "string";}
                int[]       func_arr_int()
                {
                    int result[100];
                    return result;
                }
                float[]     func_arr_float()
                {
                    float result[100];
                    return result;
                }
                boolean[]   func_arr_boolean()
                {
                    boolean result[100];
                    return result;
                }
                string[]    func_arr_string()
                {
                    string result[100];
                    return result;
                }
                void        func(int param1, float param2, string param3, boolean param4, int param5[], float param6[], string param7[], boolean param8[])
                {
                    param1 = param5[1];
                    param2 = param6[1];
                    param3 = param7[1];
                    param4 = param8[1];

                    param1 = param5[1] = param1;
                    param2 = param6[1] = param2;
                    param3 = param7[1] = param3;
                    param4 = param8[1] = param4;

                    param2 = param1;
                    param2 = param5[1];
                    param6[1] = param1;
                    param6[1] = param5[1];
                }
                int main()
                {
                    int         var_int,var_int1;
                    float       var_float,var_float1;
                    boolean     var_boolean,var_boolean1;
                    string      var_string,var_string1;
                    int         var_arr_int[100];
                    float       var_arr_float[100];
                    boolean     var_arr_boolean[100];
                    string      var_arr_string[100];

                    //assign op
                    var_int = 1;
                    var_float = 1.1;
                    var_float = 1;
                    var_boolean = true;
                    var_boolean = false;
                    var_string = "this is a string";

                    var_int = var_int1;
                    var_float = var_int1;
                    var_float = var_float1;
                    var_boolean = var_boolean1;
                    var_string = var_string1;

                    var_int = func_int();
                    var_float = func_int();
                    var_float = func_float();
                    var_boolean = func_boolean();
                    var_string = func_string();

                    var_int = var_arr_int[1];
                    var_float = var_arr_int[1];
                    var_float = var_arr_float[1];
                    var_boolean = var_arr_boolean[1];
                    var_string = var_arr_string[1];

                    var_int = func_arr_int()[1];
                    var_float = func_arr_int()[1];
                    var_float = func_arr_float()[1];
                    var_boolean = func_arr_boolean()[1];
                    var_string = func_arr_string()[1];

                    var_float = var_int = func_arr_int()[1] = var_arr_int[1] = 1;

                    // ||, &&, >, < , <=, >=
                    true || var_boolean && var_arr_boolean[1] || func_arr_boolean()[1];
                    var_int > var_float || 1 > 1.1 || var_arr_int[1] > var_arr_float[1] || func_arr_int()[1] > func_arr_float()[1];
                    var_int > var_float && 1 > 1.1 && var_arr_int[1] > var_arr_float[1] && func_arr_int()[1] > func_arr_float()[1];
                    var_int >= var_float || 1 >= 1.1 || var_arr_int[1] >= var_arr_float[1] || func_arr_int()[1] >= func_arr_float()[1];
                    var_int >= var_float && 1 >= 1.1 && var_arr_int[1] >= var_arr_float[1] && func_arr_int()[1] >= func_arr_float()[1];
                    var_int < var_float || 1 < 1.1 || var_arr_int[1] < var_arr_float[1] || func_arr_int()[1] < func_arr_float()[1];
                    var_int < var_float && 1 < 1.1 && var_arr_int[1] < var_arr_float[1] && func_arr_int()[1] < func_arr_float()[1];
                    var_int <= var_float || 1 <= 1.1 || var_arr_int[1] <= var_arr_float[1] || func_arr_int()[1] <= func_arr_float()[1];
                    var_int <= var_float && 1 <= 1.1 && var_arr_int[1] <= var_arr_float[1] && func_arr_int()[1] <= func_arr_float()[1];

                    // +, - , *, /, !=, ==
                    var_int + var_float - 1 * 1.1 / var_arr_int[1] + var_arr_float[1] - func_arr_int()[1] * func_arr_float()[1];
                    var_int + var_float > 1 * 1.1 == var_arr_int[1] + var_arr_float[1] < func_arr_int()[1] * func_arr_float()[1];
                    var_int + var_float >= 1 * 1.1 != var_arr_int[1] + var_arr_float[1] <= func_arr_int()[1] * func_arr_float()[1];
                    true || var_boolean == var_arr_boolean[1] && func_arr_boolean()[1];
                    true || var_boolean != var_arr_boolean[1] && func_arr_boolean()[1];

                    // %
                    var_int%1%var_arr_int[10]%func_int()%func_arr_int()[1];
                    // !
                    !var_boolean&&!var_arr_boolean[11]&&!func_boolean()||!func_arr_boolean()[32]||!true;
                    // -
                    -1--var_int--var_arr_int[1]--func_int()--func_arr_int()[1]--1.1--var_float--var_arr_float[1]--func_float()--func_arr_float()[1];
                    //index arr
                    var_arr_int[1 + var_int - func_int() * func_arr_int()[1]/var_arr_int[1]%1];
                    var_arr_float[1 + var_int - func_int() * func_arr_int()[1]/var_arr_int[1]%1];
                    var_arr_boolean[1 + var_int - func_int() * func_arr_int()[1]/var_arr_int[1]%1];
                    var_arr_string[1 + var_int - func_int() * func_arr_int()[1]/var_arr_int[1]%1];
                    func_arr_int()[1 + var_int - func_int() * func_arr_int()[1]/var_arr_int[1]%1];
                    func_arr_int()[1 + var_int - func_int() * func_arr_int()[1]/var_arr_int[1]%1];
                    func_arr_float()[1 + var_int - func_int() * func_arr_int()[1]/var_arr_int[1]%1];
                    func_arr_boolean()[1 + var_int - func_int() * func_arr_int()[1]/var_arr_int[1]%1];
                    func_arr_string()[1 + var_int - func_int() * func_arr_int()[1]/var_arr_int[1]%1];

                    // Call func
                    func(1, 1.5, "var_string", true, var_arr_int, var_arr_float, var_arr_string, var_arr_boolean);
                    func(var_int, var_float, var_string, var_boolean, var_arr_int, var_arr_float, var_arr_string, var_arr_boolean);
                    func(var_int, var_int, var_string, var_boolean, var_arr_int, var_arr_float, var_arr_string, var_arr_boolean);
                    func(var_arr_int[1], var_arr_float[1], var_arr_string[1], var_arr_boolean[1], var_arr_int, var_arr_float, var_arr_string, var_arr_boolean);
                    func(var_arr_int[1], var_arr_int[1], var_arr_string[1], var_arr_boolean[1], func_arr_int(), func_arr_float(), func_arr_string(), func_arr_boolean());
                    func(func_arr_int()[10], func_arr_float()[10], func_arr_string()[10], func_arr_boolean()[10], func_arr_int(), func_arr_float(), func_arr_string(), func_arr_boolean());
                    func(func_arr_int()[10], func_arr_int()[10], func_arr_string()[10], func_arr_boolean()[10], func_arr_int(), func_arr_float(), func_arr_string(), func_arr_boolean());

                    //error case
                    func(var_int, var_float, var_string, var_boolean, var_arr_int, var_arr_int, var_arr_string, var_arr_boolean);
                }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(var_int),Id(var_float),Id(var_string),Id(var_boolean),Id(var_arr_int),Id(var_arr_int),Id(var_arr_string),Id(var_arr_boolean)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_coerce_int_vs_float(self):
        input = """
                int         func_int(){return 1;}
                float       func_float(){return 1.4;}
                int[]       func_arr_int()
                {
                    int result[1];
                    return result;
                }
                float[]     func_arr_float()
                {
                    float result[1];
                    return result;
                }
                void main()
                {
                    int         var_int;
                    float       var_float;
                    int         var_arr_int[100];
                    float       var_arr_float[100];
                    var_int=func_arr_float()[1]=var_arr_float[1]=var_float=func_arr_int()[1]=var_arr_int[1]=var_int=func_int();
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(var_int),BinaryOp(=,ArrayCell(CallExpr(Id(func_arr_float),[]),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(var_arr_float),IntLiteral(1)),BinaryOp(=,Id(var_float),BinaryOp(=,ArrayCell(CallExpr(Id(func_arr_int),[]),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(var_arr_int),IntLiteral(1)),BinaryOp(=,Id(var_int),CallExpr(Id(func_int),[]))))))))"
        self.assertTrue(TestChecker.test(input,expect,400))

    #Statement
    def test_if_statement_int_exp(self):
        input = """
                void main()
                {
                    boolean var_boolean;
                    if (var_boolean)
                    {
                        var_boolean = true;
                    }

                    int var_int;
                    if (var_int)
                    {
                        var_int = 1;
                    }
                }
        """
        expect = "Type Mismatch In Statement: If(Id(var_int),Block([BinaryOp(=,Id(var_int),IntLiteral(1))]))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_if_statement_float_exp(self):
        input = """
                boolean func(){return true;}
                void main()
                {
                    boolean var_boolean;
                    if (func())
                    {
                        var_boolean = true;
                    }

                    float var_arr_float[100];
                    if (var_arr_float[1])
                    {
                        var_int = 1;
                    }
                }
        """
        expect = "Type Mismatch In Statement: If(ArrayCell(Id(var_arr_float),IntLiteral(1)),Block([BinaryOp(=,Id(var_int),IntLiteral(1))]))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_if_statement_string_exp(self):
        input = """
                string func(){return "string";}
                void main()
                {
                    boolean var_boolean[100];
                    if (var_boolean[1])
                    {
                        var_boolean[1] = true;
                    }

                    if (func())
                    {
                        true;
                    }
                }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(func),[]),Block([BooleanLiteral(true)]))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_if_else_statement_func(self):
        input = """
                boolean func(){return true;}
                void main()
                {
                    boolean var_boolean;
                    if (func())
                    {
                        var_boolean = true;
                    }
                    else
                    {
                        var_boolean = false;
                    }

                    float var_int;
                    if (func)
                    {
                        var_int = 1;
                    }
                }
        """
        expect = "Type Mismatch In Statement: If(Id(func),Block([BinaryOp(=,Id(var_int),IntLiteral(1))]))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_if_else_statement_func(self):
        input = """
                boolean func(){return true;}
                void main()
                {
                    boolean var_boolean;
                    if (func())
                    {
                        var_boolean = true;
                    }
                    else
                    {
                        var_boolean = false;
                    }

                    float var_int;
                    if (func)
                    {
                        var_int = 1;
                    }
                }
        """
        expect = "Type Mismatch In Statement: If(Id(func),Block([BinaryOp(=,Id(var_int),IntLiteral(1))]))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_for_statement(self):
        input = """
                boolean func(){return true;}
                void main()
                {
                    boolean var_boolean;
                    int i;
                    for(i = 1; func(); i = i +1)
                    {
                        var_boolean = true;
                    }

                    for(true; func(); i = i +1)
                    {
                        var_boolean = true;
                    }
                }
        """
        expect = "Type Mismatch In Statement: For(BooleanLiteral(true);CallExpr(Id(func),[]);BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(var_boolean),BooleanLiteral(true))]))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_for_statement_complex(self):
        input = """
                boolean[] func()
                {
                    boolean result[100];
                    return result;
                }
                int[] int_arr_func()
                {
                    int result[100];
                    return result;
                }
                void main()
                {
                    boolean var_boolean;
                    int i;
                    for(i = 1; func()[1]; i = i +1)
                    {
                        int i[100];
                        for(i[1] = 1; true; i[1] = i[1] +1)
                        {
                            for(int_arr_func()[1] = 1; true&&var_boolean||func()[1]; int_arr_func()[1] = int_arr_func()[1] +1)
                            {

                            }
                        }
                    }

                    for(i = 1; func()[1]; i > i +1)
                    {
                        var_boolean = true;
                    }
                }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));ArrayCell(CallExpr(Id(func),[]),IntLiteral(1));BinaryOp(>,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(var_boolean),BooleanLiteral(true))]))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_do_while_statement(self):
        input = """
                void main()
                {
                    int a,b;
                    do
                    {
                        boolean a;
                        a = true;
                    }
                    b = b - 1;
                    while a > b;

                    do
                    {
                    }
                    b = b - 1;
                    while a;
                }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([]),BinaryOp(=,Id(b),BinaryOp(-,Id(b),IntLiteral(1)))],Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_do_while_statement_complex(self):
        input = """
                void main()
                {
                    int a,b;
                    do
                    {
                        do
                        {
                            boolean a;
                            a = true;
                            do
                            {
                                boolean a;
                                a = true;
                            }
                            b = b - 1;
                            while a <= b;
                        }
                        b = b - 1;
                        while a <= b;
                    }
                    b = b - 1;
                    while a > b;
                }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_void_func(self):
        input = """
                void func_void()
                {
                    return;
                }
                void func_void2()
                {
                }
                void main()
                {
                    return 1;
                }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_int_func_1(self):
        input = """
                int func_int()
                {
                    int a;
                    return a*a+a-a/a%a+1;
                }
                int main()
                {
                    return;
                }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_int_func_2(self):
        input = """
                int func_int()
                {
                    int a;
                    return a*a+a-a/a%a+1;
                }
                int main()
                {
                    boolean a;
                    return !a&&a||a;
                }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(||,BinaryOp(&&,UnaryOp(!,Id(a)),Id(a)),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_float_func_1(self):
        input = """
                float func()
                {
                    int a;
                    return a*a+a-a/a%a+1;
                    float b;
                    return b*b+b-b/1;
                }
                float main()
                {
                    return;
                }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_float_func_2(self):
        input = """
                float func()
                {
                    int a;
                    return a*a+a-a/a%a+1;
                    float b;
                    return b*b+b-b/1;
                }
                float main()
                {
                    boolean a;
                    return !a&&a||a;
                }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(||,BinaryOp(&&,UnaryOp(!,Id(a)),Id(a)),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_string_func_1(self):
        input = """
                string func()
                {
                    string a;
                    return a;
                    string b[100];
                    return b[1];
                }
                string main()
                {
                    return;
                }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_string_func_2(self):
        input = """
                string func()
                {
                    string a;
                    return a;
                    string b[100];
                    return b[1];
                }
                string main()
                {
                    boolean a;
                    return !a&&a||a;
                }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(||,BinaryOp(&&,UnaryOp(!,Id(a)),Id(a)),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_boolean_func_1(self):
        input = """
                boolean func()
                {
                    boolean a;
                    return !a&&a||a;
                }
                boolean main()
                {
                    return;
                }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_boolean_func_2(self):
        input = """
                boolean func()
                {
                    boolean a;
                    return !a&&a||a;
                }
                boolean main()
                {
                    float b;
                    return b*b+b-b/1;
                }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(b),Id(b)),Id(b)),BinaryOp(/,Id(b),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_int_arr_func_1(self):
        input = """
                int[] func(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    int a;
                    return int_param;
                }
                int[] main(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    return;
                }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_int_arr_func_2(self):
        input = """
                int[] func(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    int a;
                    return int_param;
                }
                int[] main(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    boolean a;
                    return float_param;
                }
        """
        expect = "Type Mismatch In Statement: Return(Id(float_param))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_float_arr_func_1(self):
        input = """
                float[] func(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    int a;
                    return float_param;
                }
                float[] main(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    return;
                }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_float_arr_func_2(self):
        input = """
                float[] func(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    int a;
                    return float_param;
                }
                float[] main(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    boolean a;
                    return int_param;
                }
        """
        expect = "Type Mismatch In Statement: Return(Id(int_param))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_string_arr_func_1(self):
        input = """
                string[] func(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    string a;
                    return string_param;
                }
                string[] main(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    return;
                }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_string_arr_func_2(self):
        input = """
                string[] func(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    string a;
                    return string_param;
                }
                string[] main(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    boolean a;
                    return bool_param;
                }
        """
        expect = "Type Mismatch In Statement: Return(Id(bool_param))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_boolean_arr_func_1(self):
        input = """
                boolean[] func(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    boolean a;
                    return bool_param;
                }
                boolean[] main(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    return;
                }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_return_statement_boolean_arr_func_2(self):
        input = """
                boolean[] func(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    boolean a;
                    return bool_param;
                }
                boolean[] main(int int_param[], boolean bool_param[], string string_param[], float float_param[])
                {
                    float b;
                    return string_param;
                }
        """
        expect = "Type Mismatch In Statement: Return(Id(string_param))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_break_statement(self):
        input = """
                boolean func(){return true;}
                void main()
                {
                    boolean var_boolean;
                    int i;
                    for(i = 1; func(); i = i +1)
                    {
                        var_boolean = true;
                    }
                    int a,b;
                    do
                    {
                        boolean a;
                        a = true;
                    }
                    b = b - 1;
                    while a > b;

                    break;
                }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_continue_statement(self):
        input = """
                boolean func(){return true;}
                void main()
                {
                    boolean var_boolean;
                    int i;
                    for(i = 1; func(); i = i +1)
                    {
                        var_boolean = true;
                    }
                    int a,b;
                    do
                    {
                        boolean a;
                        a = true;
                    }
                    b = b - 1;
                    while a > b;

                    continue;
                }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_break_continue_statement_complex(self):
        input = """
                boolean func(){return true;}
                void main()
                {
                    boolean var_boolean;
                    int i;
                    for(i = 1; func(); i = i +1)
                    {
                        var_boolean = true;
                        if (var_boolean)
                        {
                            int a,b;
                            do
                            {
                                boolean a;
                                a = true;
                                do
                                {
                                    boolean a;
                                    a = true;
                                    break;
                                    continue;
                                    if (var_boolean)
                                    {
                                        break;
                                        continue;
                                    }
                                }
                                break;
                                continue;
                                b = b - 1;
                                while a;
                            }
                            b = b - 1;
                            while a <= b;
                            break;
                            continue;
                        }
                        break;
                        continue;
                    }
                    c;
                }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_func_not_return_error(self):
        input = """
                boolean func()
                {
                    return true;
                }

                int main()
                {
                    boolean var_boolean;
                    int i;
                    for(i = 1; func(); i = i +1)
                    {
                        var_boolean = true;
                        if (var_boolean)
                        {
                            int a,b;
                            do
                            {
                                boolean a;
                                a = true;
                                do
                                {
                                    boolean a;
                                    a = true;
                                    break;
                                    continue;
                                    if (var_boolean)
                                    {
                                        break;
                                        continue;
                                    }
                                }
                                break;
                                continue;
                                b = b - 1;
                                while a;
                            }
                            b = b - 1;
                            while a <= b;
                            break;
                            continue;
                        }
                        break;
                        continue;
                    }
                }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_func_not_return_error_complex(self):
        input = """
            int main(){
                boolean a1,a2,a3,a4,a5;
                if (a1){
                    if(a2){
                        if(a3){
                            if(a4){
                                return 0;
                            }
                            else{
                                return 0;
                            }
                            if(a5){
                            }
                        }else{
                            return 0;
                        }
                    }else{
                        return 0;
                    }
                }
                else{
                    if(a2){
                        if(a3){
                            if(a4){
                                return 0;
                            }
                            else{
                            }
                            if(a5){
                                return 0;
                            }
                        }else{
                            return 0;
                        }
                    }else{
                        return 0;
                    }
                }
            }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_unreachable_func(self):
        input = """
            void func1(){}
            void func2(){}
            void func3(){}
            void func4(){}
            void func5(){}
            void func6(){}
            void func7(){}
            void main(){
                func1();
                func2();
                func3();
                func5();
                func6();
                func7();
            }
        """
        expect = "Unreachable Function: func4"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_unreachable_func_complex(self):
        input = """
                int         func_int(){return 1;}
                float       func_float(){return 1;}
                boolean     func_boolean(){return true;}
                int[]       func_arr_int()
                {
                    int result[100];
                    return result;
                }
                float[]     func_arr_float()
                {
                    float result[100];
                    return result;
                }
                void main(){
                    int         var_int;
                    float       var_float;
                    int         var_arr_int[100];
                    float       var_arr_float[100];
                    func_int() + var_int > func_float() + var_float || 1 > 1.1 || var_arr_int[1] > var_arr_float[1] || func_arr_int()[1] > func_arr_float()[1];
                    func_int() + var_int > func_float() + var_float && 1 > 1.1 && var_arr_int[1] > var_arr_float[1] && func_arr_int()[1] > func_arr_float()[1];
                    func_int() + var_int >= func_float() + var_float || 1 >= 1.1 || var_arr_int[1] >= var_arr_float[1] || func_arr_int()[1] >= func_arr_float()[1];
                    func_int() + var_int >= func_float() + var_float && 1 >= 1.1 && var_arr_int[1] >= var_arr_float[1] && func_arr_int()[1] >= func_arr_float()[1];
                    func_int() + var_int < func_float() + var_float || 1 < 1.1 || var_arr_int[1] < var_arr_float[1] || func_arr_int()[1] < func_arr_float()[1];
                    func_int() + var_int < func_float() + var_float && 1 < 1.1 && var_arr_int[1] < var_arr_float[1] && func_arr_int()[1] < func_arr_float()[1];
                    func_int() + var_int <= func_float() + var_float || 1 <= 1.1 || var_arr_int[1] <= var_arr_float[1] || func_arr_int()[1] <= func_arr_float()[1];
                    func_int() + var_int <= func_float() + var_float && 1 <= 1.1 && var_arr_int[1] <= var_arr_float[1] && func_arr_int()[1] <= func_arr_float()[1];
                }
        """
        expect = "Unreachable Function: func_boolean"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_callrecusive_func(self):
        input = """
                void main(){
                    int a;
                    a = func(100);
                }
                int func(int input){
                    return input*func(input-1);
                }
                int func_test(){
                    return 0;
                }
        """
        expect = "Unreachable Function: func_test"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_arr_pnt_param(self):
        input = """
                int main(){
                    int a[100];
                    int result;
                    result = func_sum(func_transform(func_init(a,100),100),100);
                    return result;
                }

                int [] func_init(int input[], int len){
                    int i;
                    for (i=0;i<len;i = i + 1){
                        input[i] = i;
                    }
                    return input;
                }

                int [] func_transform(int input[], int len){
                    int i;
                    for (i = 0; i < len; i = i + 1){
                        if (i%4==0)
                            input[i] = input[i] * 4;
                        else if (i%4==3)
                            input[i] = input[i] * 3;
                        else if (i%4==2)
                            input[i] = input[i] * 2;
                        else
                            input[i] = input[i/2];
                    }
                    return input;
                }
                int func_sum(int input[], int len){
                    int sum;
                    sum = 0;
                    int i;
                    for (i=0;i<len;i = i + 1){
                        sum = sum + input[i];
                    }
                    return sum;
                }
                int test_arr_pnt_param(){
                    return 0;
                }
        """
        expect = "Unreachable Function: test_arr_pnt_param"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_arr_indexing_by_arr(self):
        input = """
                int main(){
                    int a[100];
                    int b[100];
                    float c[100];
                    int d[100];
                    return a[b[c[d[99]]]];
                }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),ArrayCell(Id(c),ArrayCell(Id(d),IntLiteral(99))))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_arr_indexing_by_arr_and_check_in_scope(self):
        input = """
                int main(){
                    int a[100];
                    int b[100];
                    float c[100];
                    int d[100];
                    if (true)
                    {
                        int a[100];
                        int b[100];
                        int c[100];
                        int d[100];
                        return a[b[c[d[99]]]];
                    }
                    else{

                    }
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_arr_indexing_by_arr_and_check_out_scope(self):
        input = """
                int main(){
                    int a[100];
                    int b[100];
                    float c[100];
                    int d[100];
                    if (true)
                    {
                        int a[100];
                        int b[100];
                        int c[100];
                        int d[100];
                        return a[b[c[d[99]]]];
                    }
                    else{

                    }
                    return a[b[c[d[99]]]];
                }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),ArrayCell(Id(c),ArrayCell(Id(d),IntLiteral(99))))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_call_func_by_func_type(self):
        input = """
                void main(){
                    int b;
                    b = func(func_check,b);
                }
                int func(int a, int b)
                {
                    return a + b;
                }
                int func_check(){
                    return 0;
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[Id(func_check),Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,401))