import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    ###Test Declare
    def test_declare_var(self):
        """Simple program: int main() {} """
        input = """int a;
                    boolean b;
                    float c;
                    string d;"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    def test_declare_lst_var(self):
        """Simple program: int main() {} """
        input = """int a,b,c,d;
                   boolean a,b,c,d;
                   float a,b,c,d;
                   string a,b,c,d;"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),
                            VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("d",BoolType()),
                            VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),
                            VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_arr(self):
        """Simple program: int main() {} """
        input = """int a[10];
                    boolean b[10];
                    float c[10];
                    string d[10];"""
        expect = str(Program([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,BoolType())),
            VarDecl("c",ArrayType(10,FloatType())),VarDecl("d",ArrayType(10,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_lst_arr(self):
        """Simple program: int main() {} """
        input = """int a[10],b[10],c[10],d[10];
                   boolean a[20],b[20],c[20],d[20];
                   float a[30],b[30],c[30],d[30];
                   string a[40],b[40],c[40],d[40];"""
        expect = str(Program([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,IntType())),VarDecl("c",ArrayType(10,IntType())),VarDecl("d",ArrayType(10,IntType())),
                            VarDecl("a",ArrayType(20,BoolType())),VarDecl("b",ArrayType(20,BoolType())),VarDecl("c",ArrayType(20,BoolType())),VarDecl("d",ArrayType(20,BoolType())),
                            VarDecl("a",ArrayType(30,FloatType())),VarDecl("b",ArrayType(30,FloatType())),VarDecl("c",ArrayType(30,FloatType())),VarDecl("d",ArrayType(30,FloatType())),
                            VarDecl("a",ArrayType(40,StringType())),VarDecl("b",ArrayType(40,StringType())),VarDecl("c",ArrayType(40,StringType())),VarDecl("d",ArrayType(40,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_lst_arr_var(self):
        """Simple program: int main() {} """
        input = """int a,b,c,d,a[10],b[10],c[10],d[10];
                   boolean a,b,c,d,a[20],b[20],c[20],d[20];
                   float a,b,c,d,a[30],b[30],c[30],d[30];
                   string a,b,c,d,a[40],b[40],c[40],d[40];"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),
                            VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,IntType())),VarDecl("c",ArrayType(10,IntType())),VarDecl("d",ArrayType(10,IntType())),
                            VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("d",BoolType()),
                            VarDecl("a",ArrayType(20,BoolType())),VarDecl("b",ArrayType(20,BoolType())),VarDecl("c",ArrayType(20,BoolType())),VarDecl("d",ArrayType(20,BoolType())),
                            VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),
                            VarDecl("a",ArrayType(30,FloatType())),VarDecl("b",ArrayType(30,FloatType())),VarDecl("c",ArrayType(30,FloatType())),VarDecl("d",ArrayType(30,FloatType())),
                            VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",StringType()),
                            VarDecl("a",ArrayType(40,StringType())),VarDecl("b",ArrayType(40,StringType())),VarDecl("c",ArrayType(40,StringType())),VarDecl("d",ArrayType(40,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_func(self):
        input = """int func(int a, boolean b, float c, string d){}
                   boolean func(int a, boolean b, float c, string d){}
                   float func(int a, boolean b, float c, string d){}
                   string func(int a, boolean b, float c, string d){}"""
        expect = str(Program([  FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],IntType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],BoolType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],FloatType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_arr_pnt_func(self):
        input = """int[] func(int a, boolean b, float c, string d){}
                   boolean[] func(int a, boolean b, float c, string d){}
                   float[] func(int a, boolean b, float c, string d){}
                   string[] func(int a, boolean b, float c, string d){}"""
        expect = str(Program([  FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],ArrayPointerType(IntType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],ArrayPointerType(BoolType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],ArrayPointerType(FloatType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_func_arr_pnt_param(self):
        input = """int func(int a[], boolean b[], float c[], string d[]){}
                   boolean func(int a[], boolean b[], float c[], string d[]){}
                   float func(int a[], boolean b[], float c[], string d[]){}
                   string func(int a[], boolean b[], float c[], string d[]){}"""
        expect = str(Program([  FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],IntType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],BoolType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],FloatType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_arr_pnt_func_arr_pnt_param(self):
        input = """int[] func(int a[], boolean b[], float c[], string d[]){}
                   boolean[] func(int a[], boolean b[], float c[], string d[]){}
                   float[] func(int a[], boolean b[], float c[], string d[]){}
                   string[] func(int a[], boolean b[], float c[], string d[]){}"""
        expect = str(Program([  FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(IntType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(BoolType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(FloatType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_func_mix_all(self):
        input = """int[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   boolean[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   float[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   string[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   int func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   boolean func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   float func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   string func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}"""
        expect = str(Program([  FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(IntType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(BoolType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(FloatType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],IntType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],BoolType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],FloatType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_func_empty_param(self):
        input = """int[] func(){}
                   boolean[] func(){}
                   float[] func(){}
                   string[] func(){}
                   int func(){}
                   boolean func(){}
                   float func(){}
                   string func(){}"""
        expect = str(Program([  FuncDecl(Id("func"),[],ArrayPointerType(IntType()),Block([])),
                                FuncDecl(Id("func"),[],ArrayPointerType(BoolType()),Block([])),
                                FuncDecl(Id("func"),[],ArrayPointerType(FloatType()),Block([])),
                                FuncDecl(Id("func"),[],ArrayPointerType(StringType()),Block([])),
                                FuncDecl(Id("func"),[],(IntType()),Block([])),
                                FuncDecl(Id("func"),[],(BoolType()),Block([])),
                                FuncDecl(Id("func"),[],(FloatType()),Block([])),
                                FuncDecl(Id("func"),[],(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_func_and_var_1(self):
        input = """int a,b,c,d,a[10],b[10],c[10],d[10];
                   boolean a,b,c,d,a[20],b[20],c[20],d[20];
                   float a,b,c,d,a[30],b[30],c[30],d[30];
                   string a,b,c,d,a[40],b[40],c[40],d[40];
                   int[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   boolean[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   float[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   string[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   int func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   boolean func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   float func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   string func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),
                            VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,IntType())),VarDecl("c",ArrayType(10,IntType())),VarDecl("d",ArrayType(10,IntType())),
                            VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("d",BoolType()),
                            VarDecl("a",ArrayType(20,BoolType())),VarDecl("b",ArrayType(20,BoolType())),VarDecl("c",ArrayType(20,BoolType())),VarDecl("d",ArrayType(20,BoolType())),
                            VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),
                            VarDecl("a",ArrayType(30,FloatType())),VarDecl("b",ArrayType(30,FloatType())),VarDecl("c",ArrayType(30,FloatType())),VarDecl("d",ArrayType(30,FloatType())),
                            VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",StringType()),
                            VarDecl("a",ArrayType(40,StringType())),VarDecl("b",ArrayType(40,StringType())),VarDecl("c",ArrayType(40,StringType())),VarDecl("d",ArrayType(40,StringType())),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(IntType()),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(BoolType()),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(FloatType()),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],IntType(),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],BoolType(),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],FloatType(),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_func_and_var_2(self):
        input = """int[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   boolean[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   float[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   string[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   int func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   boolean func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   float func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   string func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   int a,b,c,d,a[10],b[10],c[10],d[10];
                   boolean a,b,c,d,a[20],b[20],c[20],d[20];
                   float a,b,c,d,a[30],b[30],c[30],d[30];
                   string a,b,c,d,a[40],b[40],c[40],d[40];"""
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(IntType()),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(BoolType()),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(FloatType()),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],IntType(),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],BoolType(),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],FloatType(),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],StringType(),Block([])),
                            VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,IntType())),VarDecl("c",ArrayType(10,IntType())),VarDecl("d",ArrayType(10,IntType())),
                            VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("d",BoolType()),VarDecl("a",ArrayType(20,BoolType())),VarDecl("b",ArrayType(20,BoolType())),VarDecl("c",ArrayType(20,BoolType())),VarDecl("d",ArrayType(20,BoolType())),
                            VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("a",ArrayType(30,FloatType())),VarDecl("b",ArrayType(30,FloatType())),VarDecl("c",ArrayType(30,FloatType())),VarDecl("d",ArrayType(30,FloatType())),
                            VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",StringType()),VarDecl("a",ArrayType(40,StringType())),VarDecl("b",ArrayType(40,StringType())),VarDecl("c",ArrayType(40,StringType())),VarDecl("d",ArrayType(40,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_func_and_var_3(self):
        input = """int[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   boolean[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   int a,b,c,d,a[10],b[10],c[10],d[10];
                   float[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   string[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   boolean a,b,c,d,a[20],b[20],c[20],d[20];
                   int func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   boolean func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   float a,b,c,d,a[30],b[30],c[30],d[30];
                   float func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   string func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                   string a,b,c,d,a[40],b[40],c[40],d[40];"""
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(IntType()),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(BoolType()),Block([])),
                            VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,IntType())),VarDecl("c",ArrayType(10,IntType())),VarDecl("d",ArrayType(10,IntType())),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(FloatType()),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([])),
                            VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("d",BoolType()),VarDecl("a",ArrayType(20,BoolType())),VarDecl("b",ArrayType(20,BoolType())),VarDecl("c",ArrayType(20,BoolType())),VarDecl("d",ArrayType(20,BoolType())),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],IntType(),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],BoolType(),Block([])),
                            VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("a",ArrayType(30,FloatType())),VarDecl("b",ArrayType(30,FloatType())),VarDecl("c",ArrayType(30,FloatType())),VarDecl("d",ArrayType(30,FloatType())),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],FloatType(),Block([])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],StringType(),Block([])),
                            VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",StringType()),VarDecl("a",ArrayType(40,StringType())),VarDecl("b",ArrayType(40,StringType())),VarDecl("c",ArrayType(40,StringType())),VarDecl("d",ArrayType(40,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_declare_func_and_local_var(self):
        input = """int[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                    {
                        int a,b,c,d,a[10],b[10],c[10],d[10];
                    }
                   boolean[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                   {
                        int a,b,c,d,a[10],b[10],c[10],d[10];
                   }
                   float[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                   {
                        boolean a,b,c,d,a[20],b[20],c[20],d[20];
                   }
                   string[] func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                   {
                        boolean a,b,c,d,a[20],b[20],c[20],d[20];
                   }
                   
                   int func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                   {
                        float a,b,c,d,a[30],b[30],c[30],d[30];
                   }
                   boolean func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                   {
                        float a,b,c,d,a[30],b[30],c[30],d[30];
                   }
                   
                   float func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                   {
                        string a,b,c,d,a[40],b[40],c[40],d[40];
                   }
                   string func(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                   {
                        string a,b,c,d,a[40],b[40],c[40],d[40];
                   }
                   """
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(IntType()),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,IntType())),VarDecl("c",ArrayType(10,IntType())),VarDecl("d",ArrayType(10,IntType()))])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(BoolType()),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,IntType())),VarDecl("c",ArrayType(10,IntType())),VarDecl("d",ArrayType(10,IntType()))])),

                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(FloatType()),Block([VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("d",BoolType()),VarDecl("a",ArrayType(20,BoolType())),VarDecl("b",ArrayType(20,BoolType())),VarDecl("c",ArrayType(20,BoolType())),VarDecl("d",ArrayType(20,BoolType()))])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("d",BoolType()),VarDecl("a",ArrayType(20,BoolType())),VarDecl("b",ArrayType(20,BoolType())),VarDecl("c",ArrayType(20,BoolType())),VarDecl("d",ArrayType(20,BoolType()))])),
                            
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("a",ArrayType(30,FloatType())),VarDecl("b",ArrayType(30,FloatType())),VarDecl("c",ArrayType(30,FloatType())),VarDecl("d",ArrayType(30,FloatType()))])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],BoolType(),Block([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("a",ArrayType(30,FloatType())),VarDecl("b",ArrayType(30,FloatType())),VarDecl("c",ArrayType(30,FloatType())),VarDecl("d",ArrayType(30,FloatType()))])),
                            
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],FloatType(),Block([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",StringType()),VarDecl("a",ArrayType(40,StringType())),VarDecl("b",ArrayType(40,StringType())),VarDecl("c",ArrayType(40,StringType())),VarDecl("d",ArrayType(40,StringType()))])),
                            FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType()),VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],StringType(),Block([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",StringType()),VarDecl("a",ArrayType(40,StringType())),VarDecl("b",ArrayType(40,StringType())),VarDecl("c",ArrayType(40,StringType())),VarDecl("d",ArrayType(40,StringType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
        # -> miss void func
    ###Test expression
    def test_expr_ID(self):
        input = """void func()
                {
                    a;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([Id("a")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    def test_expr_func_call(self):
        input = """void func()
                {
                    funccall(a,1,"b",1.1,false);
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([CallExpr(Id("funccall"),[Id('a'),IntLiteral(1),StringLiteral('b'),FloatLiteral(1.1),BooleanLiteral(False)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_expr_ArrayCell(self):
        input = """void func()
                {
                    a[1];
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([ArrayCell(Id("a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    def test_expr_FuncArrayCell(self):
        input = """void func()
                {
                    abc()[10];
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([ArrayCell(CallExpr(Id("abc"),[]),IntLiteral(10))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    def test_expr_int_lit(self):
        input = """void func()
                {
                    123;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([IntLiteral(123)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    def test_expr_bool_lit(self):
        input = """void func()
                {
                    true;
                    false;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BooleanLiteral(True),BooleanLiteral(False)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    def test_expr_string_lit(self):
        input = """void func()
                {
                    "This is a string";
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([StringLiteral("This is a string")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_expr_float_lit(self):
        input = """void func()
                {
                    1.2; 1.; .11;
                    1.2E5; 1.2e5; .1E2; .1e5;
                    1.2E-5; 1.2e-5; .1E-2; .1e-5;
                    1.E-5; 1.e-5;
                    1E-5; 1e-5;
                    1E5; 1e5;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([FloatLiteral(1.2),FloatLiteral(1.),FloatLiteral(.11),FloatLiteral(1.2E5),
            FloatLiteral(1.2e5),FloatLiteral(.1E2),FloatLiteral(.1e5),FloatLiteral(1.2E-5),FloatLiteral(1.2e-5),FloatLiteral(.1E-2),FloatLiteral(.1e-5),
            FloatLiteral(1.E-5),FloatLiteral(1.e-5),FloatLiteral(1E-5),FloatLiteral(1e-5),FloatLiteral(1E5),FloatLiteral(1e5)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    def test_expr_assign(self):
        input = """void func()
                {
                    a = b;
                    a = "String";
                    a[1] = 1;
                    a = true;
                    a = false;
                    a()[1] = 1e3;
                    a = funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("=",Id('a'),Id('b')),BinaryOp("=",Id('a'),StringLiteral('String')),
            BinaryOp("=",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp("=",Id('a'),BooleanLiteral(True)),BinaryOp("=",Id('a'),BooleanLiteral(False)),
            BinaryOp("=",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp("=",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_expr_assign_assosiate(self):
        input = """void func()
                {
                    a = b[1] = c()[1] = false;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("=",Id('a'),BinaryOp('=',ArrayCell(Id('b'),IntLiteral(1)),BinaryOp('=',ArrayCell(CallExpr(Id('c'),[]),IntLiteral(1)),BooleanLiteral(False))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

'''
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
'''