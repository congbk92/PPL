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
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
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
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_declare_arr(self):
        """Simple program: int main() {} """
        input = """int a[10];
                    boolean b[10];
                    float c[10];
                    string d[10];"""
        expect = str(Program([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",ArrayType(10,BoolType())),
            VarDecl("c",ArrayType(10,FloatType())),VarDecl("d",ArrayType(10,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

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
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

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
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_declare_func(self):
        input = """int func(int a, boolean b, float c, string d){}
                   boolean func(int a, boolean b, float c, string d){}
                   float func(int a, boolean b, float c, string d){}
                   string func(int a, boolean b, float c, string d){}"""
        expect = str(Program([  FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],IntType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],BoolType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],FloatType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_declare_arr_pnt_func(self):
        input = """int[] func(int a, boolean b, float c, string d){}
                   boolean[] func(int a, boolean b, float c, string d){}
                   float[] func(int a, boolean b, float c, string d){}
                   string[] func(int a, boolean b, float c, string d){}"""
        expect = str(Program([  FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],ArrayPointerType(IntType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],ArrayPointerType(BoolType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],ArrayPointerType(FloatType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",FloatType()),VarDecl("d",StringType())],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_declare_func_arr_pnt_param(self):
        input = """int func(int a[], boolean b[], float c[], string d[]){}
                   boolean func(int a[], boolean b[], float c[], string d[]){}
                   float func(int a[], boolean b[], float c[], string d[]){}
                   string func(int a[], boolean b[], float c[], string d[]){}"""
        expect = str(Program([  FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],IntType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],BoolType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],FloatType(),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_declare_arr_pnt_func_arr_pnt_param(self):
        input = """int[] func(int a[], boolean b[], float c[], string d[]){}
                   boolean[] func(int a[], boolean b[], float c[], string d[]){}
                   float[] func(int a[], boolean b[], float c[], string d[]){}
                   string[] func(int a[], boolean b[], float c[], string d[]){}"""
        expect = str(Program([  FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(IntType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(BoolType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(FloatType()),Block([])),
                                FuncDecl(Id("func"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",ArrayPointerType(BoolType())),VarDecl("c",ArrayPointerType(FloatType())),VarDecl("d",ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

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
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

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
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

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
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

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
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

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
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

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
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
        # -> miss void func
    ###Test expression
    def test_expr_ID(self):
        input = """void func()
                {
                    a;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([Id("a")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_expr_func_call(self):
        input = """void func()
                {
                    funccall(a,1,"b",1.1,false,a[1],func());
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            CallExpr(Id("funccall"),[Id('a'),IntLiteral(1),StringLiteral('b'),FloatLiteral(1.1),BooleanLiteral(False),ArrayCell(Id("a"),IntLiteral(1)),CallExpr(Id("func"),[])])
            ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_expr_func_call_complex(self):
        input = """void func()
                {
                    funccall(funccall(funccall(),funccall()),funccall(funccall(),funccall()));
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([ #CallExpr(Id("funccall"),[])
            CallExpr(Id("funccall"),[CallExpr(Id("funccall"),[CallExpr(Id("funccall"),[]),CallExpr(Id("funccall"),[])]),CallExpr(Id("funccall"),[CallExpr(Id("funccall"),[]),CallExpr(Id("funccall"),[])])])
            ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_expr_ArrayCell(self):
        input = """void func()
                {
                    a[1];
                    a[a];
                    a["string"];
                    a[1.1];
                    a[true];
                    a[false];
                    a[func()];
                    a[func()[1]];
                    a[a[1]];
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            ArrayCell(Id("a"),IntLiteral(1)),
            ArrayCell(Id("a"),Id("a")),
            ArrayCell(Id("a"),StringLiteral("string")),
            ArrayCell(Id("a"),FloatLiteral(1.1)),
            ArrayCell(Id("a"),BooleanLiteral(True)),
            ArrayCell(Id("a"),BooleanLiteral(False)),
            ArrayCell(Id("a"),CallExpr(Id("func"),[])),
            ArrayCell(Id("a"),ArrayCell(CallExpr(Id("func"),[]),IntLiteral(1))),
            ArrayCell(Id("a"),ArrayCell(Id("a"),IntLiteral(1))),
            ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_expr_ArrayCell_complex(self):
        input = """void func()
                {
                    a[a[a[a[a[1]]]]];
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),IntLiteral(1))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_expr_FuncArrayCell(self):
        input = """void func()
                {
                    abc()[10];
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([ArrayCell(CallExpr(Id("abc"),[]),IntLiteral(10))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_expr_FuncArrayCell_complex_1(self):
        input = """void func()
                {
                    a(a(a()[1],a()[1])[1],a(a()[1],a()[1])[1])[1];
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            ArrayCell(CallExpr(Id("a"),[ArrayCell(CallExpr(Id("a"),[ArrayCell(CallExpr(Id("a"),[]),IntLiteral(1)),ArrayCell(CallExpr(Id("a"),[]),IntLiteral(1))]),IntLiteral(1)),
            ArrayCell(CallExpr(Id("a"),[ArrayCell(CallExpr(Id("a"),[]),IntLiteral(1)),ArrayCell(CallExpr(Id("a"),[]),IntLiteral(1))]),IntLiteral(1))]),IntLiteral(1))
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_expr_FuncArrayCell_complex_2(self):
        input = """void func()
                {
                    a()[a()[a()[a()[a()[a()]]]]];
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            ArrayCell(CallExpr(Id("a"),[]), ArrayCell(CallExpr(Id("a"),[]), ArrayCell(CallExpr(Id("a"),[]), ArrayCell(CallExpr(Id("a"),[]), ArrayCell(CallExpr(Id("a"),[]),CallExpr(Id("a"),[]))))))
            ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_expr_FuncArrayCell_complex_3(self):
        input = """void func()
                {
                    a(a()[a()[a()[1]]])[a(a()[a()[a()[1]]])[a(a()[a()[a()[1]]])[1]]];
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            ArrayCell(CallExpr(Id("a"),[ArrayCell(CallExpr(Id("a"),[]),ArrayCell(CallExpr(Id("a"),[]),ArrayCell(CallExpr(Id("a"),[]),IntLiteral(1))))]),ArrayCell(CallExpr(Id("a"),[ArrayCell(CallExpr(Id("a"),[]),ArrayCell(CallExpr(Id("a"),[]),ArrayCell(CallExpr(Id("a"),[]),IntLiteral(1))))]),ArrayCell(CallExpr(Id("a"),[ArrayCell(CallExpr(Id("a"),[]),ArrayCell(CallExpr(Id("a"),[]),ArrayCell(CallExpr(Id("a"),[]),IntLiteral(1))))]),IntLiteral(1))))
            ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_expr_int_lit(self):
        input = """void func()
                {
                    123;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([IntLiteral(123)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_expr_bool_lit(self):
        input = """void func()
                {
                    true;
                    false;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BooleanLiteral(True),BooleanLiteral(False)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_expr_string_lit(self):
        input = """void func()
                {
                    "This is a string";
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([StringLiteral("This is a string")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

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
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
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
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_expr_assign_assosiate(self):
        input = """void func()
                {
                    a = b[1] = c()[1] = false;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("=",Id('a'),BinaryOp('=',ArrayCell(Id('b'),IntLiteral(1)),BinaryOp('=',ArrayCell(CallExpr(Id('c'),[]),IntLiteral(1)),BooleanLiteral(False))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_expr_or(self):
        input = """void func()
                {
                    a || b; a || "String"; a[1] || 1; a || true; a || false; a()[1] || 1e3; a || funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("||",Id('a'),Id('b')),BinaryOp("||",Id('a'),StringLiteral('String')),
            BinaryOp("||",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp("||",Id('a'),BooleanLiteral(True)),BinaryOp("||",Id('a'),BooleanLiteral(False)),
            BinaryOp("||",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp("||",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_expr_or_associate(self):
        input = """void func()
                {
                    a || b[1] || c()[1] || false;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("||",BinaryOp("||",BinaryOp("||",Id('a'),ArrayCell(Id('b'),IntLiteral(1))),ArrayCell(CallExpr(Id('c'),[]),IntLiteral(1))),BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    
    def test_expr_and(self):
        input = """void func()
                {
                    a && b; a && "String"; a[1] && 1; a && true; a && false; a()[1] && 1e3; a && funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("&&",Id('a'),Id('b')),BinaryOp("&&",Id('a'),StringLiteral('String')),
            BinaryOp("&&",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp("&&",Id('a'),BooleanLiteral(True)),BinaryOp("&&",Id('a'),BooleanLiteral(False)),
            BinaryOp("&&",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp("&&",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_expr_and_associate(self):
        input = """void func()
                {
                    a && b[1] && c()[1] && false;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("&&",BinaryOp("&&",BinaryOp("&&",Id('a'),ArrayCell(Id('b'),IntLiteral(1))),ArrayCell(CallExpr(Id('c'),[]),IntLiteral(1))),BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    
    def test_expr_equal(self):
        input = """void func()
                {
                    a == b; a == "String"; a[1] == 1; a == true; a == false; a()[1] == 1e3; a == funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("==",Id('a'),Id('b')),BinaryOp("==",Id('a'),StringLiteral('String')),
            BinaryOp("==",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp("==",Id('a'),BooleanLiteral(True)),BinaryOp("==",Id('a'),BooleanLiteral(False)),
            BinaryOp("==",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp("==",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    
    def test_expr_diff(self):
        input = """void func()
                {
                    a != b; a != "String"; a[1] != 1; a != true; a != false; a()[1] != 1e3; a != funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("!=",Id('a'),Id('b')),BinaryOp("!=",Id('a'),StringLiteral('String')),
            BinaryOp("!=",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp("!=",Id('a'),BooleanLiteral(True)),BinaryOp("!=",Id('a'),BooleanLiteral(False)),
            BinaryOp("!=",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp("!=",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    
    def test_expr_greater(self):
        input = """void func()
                {
                    a > b; a > "String"; a[1] > 1; a > true; a > false; a()[1] > 1e3; a > funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp(">",Id('a'),Id('b')),BinaryOp(">",Id('a'),StringLiteral('String')),
            BinaryOp(">",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp(">",Id('a'),BooleanLiteral(True)),BinaryOp(">",Id('a'),BooleanLiteral(False)),
            BinaryOp(">",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp(">",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    
    def test_expr_greater_equal(self):
        input = """void func()
                {
                    a >= b; a >= "String"; a[1] >= 1; a >= true; a >= false; a()[1] >= 1e3; a >= funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp(">=",Id('a'),Id('b')),BinaryOp(">=",Id('a'),StringLiteral('String')),
            BinaryOp(">=",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp(">=",Id('a'),BooleanLiteral(True)),BinaryOp(">=",Id('a'),BooleanLiteral(False)),
            BinaryOp(">=",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp(">=",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    
    def test_expr_smaller(self):
        input = """void func()
                {
                    a < b; a < "String"; a[1] < 1; a < true; a < false; a()[1] < 1e3; a < funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("<",Id('a'),Id('b')),BinaryOp("<",Id('a'),StringLiteral('String')),
            BinaryOp("<",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp("<",Id('a'),BooleanLiteral(True)),BinaryOp("<",Id('a'),BooleanLiteral(False)),
            BinaryOp("<",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp("<",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    
    def test_expr_smaller_equal(self):
        input = """void func()
                {
                    a <= b; a <= "String"; a[1] <= 1; a <= true; a <= false; a()[1] <= 1e3; a <= funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("<=",Id('a'),Id('b')),BinaryOp("<=",Id('a'),StringLiteral('String')),
            BinaryOp("<=",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp("<=",Id('a'),BooleanLiteral(True)),BinaryOp("<=",Id('a'),BooleanLiteral(False)),
            BinaryOp("<=",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp("<=",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
        
    def test_expr_add(self):
        input = """void func()
                {
                    a + b; a + "String"; a[1] + 1; a + true; a + false; a()[1] + 1e3; a + funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("+",Id('a'),Id('b')),BinaryOp("+",Id('a'),StringLiteral('String')),
            BinaryOp("+",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp("+",Id('a'),BooleanLiteral(True)),BinaryOp("+",Id('a'),BooleanLiteral(False)),
            BinaryOp("+",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp("+",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_expr_add_associate(self):
        input = """void func()
                {
                    a + b[1] + c()[1] + false;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("+",BinaryOp("+",BinaryOp("+",Id('a'),ArrayCell(Id('b'),IntLiteral(1))),ArrayCell(CallExpr(Id('c'),[]),IntLiteral(1))),BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_expr_sub(self):
        input = """void func()
                {
                    a - b; a - "String"; a[1] - 1; a - true; a - false; a()[1] - 1e3; a - funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("-",Id('a'),Id('b')),BinaryOp("-",Id('a'),StringLiteral('String')),
            BinaryOp("-",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp("-",Id('a'),BooleanLiteral(True)),BinaryOp("-",Id('a'),BooleanLiteral(False)),
            BinaryOp("-",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp("-",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_expr_sub_associate(self):
        input = """void func()
                {
                    a - b[1] - c()[1] - false;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("-",BinaryOp("-",BinaryOp("-",Id('a'),ArrayCell(Id('b'),IntLiteral(1))),ArrayCell(CallExpr(Id('c'),[]),IntLiteral(1))),BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_expr_div(self):
        input = """void func()
                {
                    a / b; a / "String"; a[1] / 1; a / true; a / false; a()[1] / 1e3; a / funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("/",Id('a'),Id('b')),BinaryOp("/",Id('a'),StringLiteral('String')),
            BinaryOp("/",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp("/",Id('a'),BooleanLiteral(True)),BinaryOp("/",Id('a'),BooleanLiteral(False)),
            BinaryOp("/",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp("/",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_expr_div_associate(self):
        input = """void func()
                {
                    a / b[1] / c()[1] / false;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("/",BinaryOp("/",BinaryOp("/",Id('a'),ArrayCell(Id('b'),IntLiteral(1))),ArrayCell(CallExpr(Id('c'),[]),IntLiteral(1))),BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    
    def test_expr_mul(self):
        input = """void func()
                {
                    a * b; a * "String"; a[1] * 1; a * true; a * false; a()[1] * 1e3; a * funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("*",Id('a'),Id('b')),BinaryOp("*",Id('a'),StringLiteral('String')),
            BinaryOp("*",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp("*",Id('a'),BooleanLiteral(True)),BinaryOp("*",Id('a'),BooleanLiteral(False)),
            BinaryOp("*",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp("*",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_expr_mul_associate(self):
        input = """void func()
                {
                    a * b[1] * c()[1] * false;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("*",BinaryOp("*",BinaryOp("*",Id('a'),ArrayCell(Id('b'),IntLiteral(1))),ArrayCell(CallExpr(Id('c'),[]),IntLiteral(1))),BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_expr_mod(self):
        input = """void func()
                {
                    a % b; a % "String"; a[1] % 1; a % true; a % false; a()[1] % 1e3; a % funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("%",Id('a'),Id('b')),BinaryOp("%",Id('a'),StringLiteral('String')),
            BinaryOp("%",ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp("%",Id('a'),BooleanLiteral(True)),BinaryOp("%",Id('a'),BooleanLiteral(False)),
            BinaryOp("%",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1)),FloatLiteral(1e3)),BinaryOp("%",Id('a'),CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_expr_mod_associate(self):
        input = """void func()
                {
                    a % b[1] % c()[1] % false;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([BinaryOp("%",BinaryOp("%",BinaryOp("%",Id('a'),ArrayCell(Id('b'),IntLiteral(1))),ArrayCell(CallExpr(Id('c'),[]),IntLiteral(1))),BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    
    def test_expr_unary_sub(self):
        input = """void func()
                {
                    -"String"; -true; -false; -1e3; -2; -a; -a[1]; -a()[1]; -funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        UnaryOp("-",StringLiteral("String")),
        UnaryOp("-",BooleanLiteral(True)),
        UnaryOp("-",BooleanLiteral(False)),
        UnaryOp("-",FloatLiteral(1e3)),
        UnaryOp("-",IntLiteral(2)),
        UnaryOp("-",Id("a")),
        UnaryOp("-",ArrayCell(Id('a'),IntLiteral(1))),
        UnaryOp("-",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1))),
        UnaryOp("-",CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_expr_unary_sub_associate(self):
        input = """void func()
                {
                    ---"String"; ---true; ---false; ---1e3; ---2; ---a; ---a[1]; ---a()[1]; ---funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        UnaryOp("-",UnaryOp("-",UnaryOp("-",StringLiteral("String")))),
        UnaryOp("-",UnaryOp("-",UnaryOp("-",BooleanLiteral(True)))),
        UnaryOp("-",UnaryOp("-",UnaryOp("-",BooleanLiteral(False)))),
        UnaryOp("-",UnaryOp("-",UnaryOp("-",FloatLiteral(1e3)))),
        UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(2)))),
        UnaryOp("-",UnaryOp("-",UnaryOp("-",Id("a")))),
        UnaryOp("-",UnaryOp("-",UnaryOp("-",ArrayCell(Id('a'),IntLiteral(1))))),
        UnaryOp("-",UnaryOp("-",UnaryOp("-",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1))))),
        UnaryOp("-",UnaryOp("-",UnaryOp("-",CallExpr(Id('funcABC'),[]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    
    def test_expr_unary_sub_associate_1(self):
        input = """void func()
                {
                    a---b;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("-",Id("a"),UnaryOp("-",UnaryOp("-",Id("b"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    
    def test_expr_not(self):
        input = """void func()
                {
                    !"String"; !true; !false; !1e3; !2; !a; !a[1]; !a()[1]; !funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        UnaryOp("!",StringLiteral("String")),
        UnaryOp("!",BooleanLiteral(True)),
        UnaryOp("!",BooleanLiteral(False)),
        UnaryOp("!",FloatLiteral(1e3)),
        UnaryOp("!",IntLiteral(2)),
        UnaryOp("!",Id("a")),
        UnaryOp("!",ArrayCell(Id('a'),IntLiteral(1))),
        UnaryOp("!",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1))),
        UnaryOp("!",CallExpr(Id('funcABC'),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_expr_not_associate(self):
        input = """void func()
                {
                    !!!"String"; !!!true; !!!false; !!!1e3; !!!2; !!!a; !!!a[1]; !!!a()[1]; !!!funcABC();
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        UnaryOp("!",UnaryOp("!",UnaryOp("!",StringLiteral("String")))),
        UnaryOp("!",UnaryOp("!",UnaryOp("!",BooleanLiteral(True)))),
        UnaryOp("!",UnaryOp("!",UnaryOp("!",BooleanLiteral(False)))),
        UnaryOp("!",UnaryOp("!",UnaryOp("!",FloatLiteral(1e3)))),
        UnaryOp("!",UnaryOp("!",UnaryOp("!",IntLiteral(2)))),
        UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("a")))),
        UnaryOp("!",UnaryOp("!",UnaryOp("!",ArrayCell(Id('a'),IntLiteral(1))))),
        UnaryOp("!",UnaryOp("!",UnaryOp("!",ArrayCell(CallExpr(Id('a'),[]),IntLiteral(1))))),
        UnaryOp("!",UnaryOp("!",UnaryOp("!",CallExpr(Id('funcABC'),[]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_expr_precedence_lv23(self):
        input = """void func()
                {
                    a/-b*-c%-d;
                    a/!b*!c%!d;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("%",BinaryOp("*",BinaryOp("/",Id('a'),UnaryOp("-",Id("b"))),UnaryOp("-",Id("c"))),UnaryOp("-",Id("d"))),
        BinaryOp("%",BinaryOp("*",BinaryOp("/",Id('a'),UnaryOp("!",Id("b"))),UnaryOp("!",Id("c"))),UnaryOp("!",Id("d")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    
    def test_expr_precedence_lv34(self):
        input = """void func()
                {
                    a + b/c - d/e;
                    a + b*c - d*e;
                    a + b%c - d%e;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("-",BinaryOp("+",Id("a"),BinaryOp("/",Id("b"),Id("c"))),BinaryOp("/",Id("d"),Id("e"))),
        BinaryOp("-",BinaryOp("+",Id("a"),BinaryOp("*",Id("b"),Id("c"))),BinaryOp("*",Id("d"),Id("e"))),
        BinaryOp("-",BinaryOp("+",Id("a"),BinaryOp("%",Id("b"),Id("c"))),BinaryOp("%",Id("d"),Id("e")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test_expr_precedence_lv45(self):
        input = """void func()
                {
                    a + b <  c - d;
                    a + b <= c - d;
                    a + b >  c - d;
                    a + b >= c - d;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),
        BinaryOp("<=",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),
        BinaryOp(">",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),
        BinaryOp(">=",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
        
    def test_expr_precedence_lv56(self):
        input = """void func()
                {
                    a < b == c < d;
                    a < b != c < d;
                    a <=b == c <=d;
                    a <=b != c <=d;
                    a > b == c > d;
                    a > b != c > d;
                    a >=b == c >=d;
                    a >=b != c >=d;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("==",BinaryOp("<",Id("a"),Id("b")),BinaryOp("<",Id("c"),Id("d"))),
        BinaryOp("!=",BinaryOp("<",Id("a"),Id("b")),BinaryOp("<",Id("c"),Id("d"))),
        BinaryOp("==",BinaryOp("<=",Id("a"),Id("b")),BinaryOp("<=",Id("c"),Id("d"))),
        BinaryOp("!=",BinaryOp("<=",Id("a"),Id("b")),BinaryOp("<=",Id("c"),Id("d"))),
        BinaryOp("==",BinaryOp(">",Id("a"),Id("b")),BinaryOp(">",Id("c"),Id("d"))),
        BinaryOp("!=",BinaryOp(">",Id("a"),Id("b")),BinaryOp(">",Id("c"),Id("d"))),
        BinaryOp("==",BinaryOp(">=",Id("a"),Id("b")),BinaryOp(">=",Id("c"),Id("d"))),
        BinaryOp("!=",BinaryOp(">=",Id("a"),Id("b")),BinaryOp(">=",Id("c"),Id("d")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    
    def test_expr_precedence_lv67(self):
        input = """void func()
                {
                    a == b && c == d;
                    a != b && c != d;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("&&",BinaryOp("==",Id("a"),Id("b")),BinaryOp("==",Id("c"),Id("d"))),
        BinaryOp("&&",BinaryOp("!=",Id("a"),Id("b")),BinaryOp("!=",Id("c"),Id("d")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_expr_precedence_lv78(self):
        input = """void func()
                {
                    a && b || c && d;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("||",BinaryOp("&&",Id("a"),Id("b")),BinaryOp("&&",Id("c"),Id("d")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
        
    def test_expr_precedence_lv89(self):
        input = """void func()
                {
                    a = b || c || d;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("=",Id("a"),BinaryOp("||",BinaryOp("||",Id("b"),Id("c")),Id("d")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))


    def test_expr_precedence_highest_89(self):
        input = """void func()
                {
                    (a = b) || (c = d);
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("||",BinaryOp("=",Id("a"),Id("b")),BinaryOp("=",Id("c"),Id("d"))),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))


    def test_expr_precedence_highest_78(self):
        input = """void func()
                {
                    (a || b) && (c || d);
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("&&",BinaryOp("||",Id("a"),Id("b")),BinaryOp("||",Id("c"),Id("d"))),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))


    def test_expr_precedence_highest_67(self):
        input = """void func()
                {
                    (a && b) == (c && d);
                    (a && b) != (c && d); 
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("==",BinaryOp("&&",Id("a"),Id("b")),BinaryOp("&&",Id("c"),Id("d"))),
        BinaryOp("!=",BinaryOp("&&",Id("a"),Id("b")),BinaryOp("&&",Id("c"),Id("d"))),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))


    def test_expr_precedence_highest_56(self):
        input = """void func()
                {
                    (a == b) < (c == d);
                    (a != b) < (c != d);
                    (a == b)<= (c == d);
                    (a != b)<= (c != d);
                    (a == b) > (c == d);
                    (a != b) > (c != d);                    
                    (a == b)>= (c == d);
                    (a != b)>= (c != d);
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("<",BinaryOp("==",Id("a"),Id("b")),BinaryOp("==",Id("c"),Id("d"))),
        BinaryOp("<",BinaryOp("!=",Id("a"),Id("b")),BinaryOp("!=",Id("c"),Id("d"))),
        BinaryOp("<=",BinaryOp("==",Id("a"),Id("b")),BinaryOp("==",Id("c"),Id("d"))),
        BinaryOp("<=",BinaryOp("!=",Id("a"),Id("b")),BinaryOp("!=",Id("c"),Id("d"))),
        BinaryOp(">",BinaryOp("==",Id("a"),Id("b")),BinaryOp("==",Id("c"),Id("d"))),
        BinaryOp(">",BinaryOp("!=",Id("a"),Id("b")),BinaryOp("!=",Id("c"),Id("d"))),
        BinaryOp(">=",BinaryOp("==",Id("a"),Id("b")),BinaryOp("==",Id("c"),Id("d"))),
        BinaryOp(">=",BinaryOp("!=",Id("a"),Id("b")),BinaryOp("!=",Id("c"),Id("d"))),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))


    def test_expr_precedence_highest_45(self):
        input = """void func()
                {
                    a + (b > c) - (d > e);
                    a + (b >= c) - (d >= e);
                    a + (b < c) - (d < e);
                    a + (b <= c) - (d <= e);
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("-",BinaryOp("+",Id("a"),BinaryOp(">",Id("b"),Id("c"))),BinaryOp(">",Id("d"),Id("e"))),
        BinaryOp("-",BinaryOp("+",Id("a"),BinaryOp(">=",Id("b"),Id("c"))),BinaryOp(">=",Id("d"),Id("e"))),
        BinaryOp("-",BinaryOp("+",Id("a"),BinaryOp("<",Id("b"),Id("c"))),BinaryOp("<",Id("d"),Id("e"))),
        BinaryOp("-",BinaryOp("+",Id("a"),BinaryOp("<=",Id("b"),Id("c"))),BinaryOp("<=",Id("d"),Id("e"))),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))


    def test_expr_precedence_highest_34(self):
        input = """void func()
                {
                    (a+b)*(c-d);
                    (a+b)/(c-d);
                    (a+b)%(c-d);
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("*",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),
        BinaryOp("/",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),
        BinaryOp("%",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))


    def test_expr_precedence_highest_23(self):
        input = """void func()
                {
                    -(a*b)--(c/d)--(e%f);
                    !(a*b)-!(c/d)-!(e%f);                   
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("-",BinaryOp("-",UnaryOp("-",BinaryOp("*",Id("a"),Id("b"))),UnaryOp("-",BinaryOp("/",Id("c"),Id("d")))),UnaryOp("-",BinaryOp("%",Id("e"),Id("f")))),
        BinaryOp("-",BinaryOp("-",UnaryOp("!",BinaryOp("*",Id("a"),Id("b"))),UnaryOp("!",BinaryOp("/",Id("c"),Id("d")))),UnaryOp("!",BinaryOp("%",Id("e"),Id("f")))),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_expr_precedence_for_decimal_operand(self):
        input = """void func()
                {
                    a = a*-b[1] + a/-b[1] - a%-b[1];
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("+",BinaryOp("*",Id("a"),UnaryOp("-",ArrayCell(Id("b"),IntLiteral(1)))),BinaryOp("/",Id("a"),UnaryOp("-",ArrayCell(Id("b"),IntLiteral(1))))),BinaryOp("%",Id("a"),UnaryOp("-",ArrayCell(Id("b"),IntLiteral(1))))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_expr_precedence_for_binary_operand(self):
        input = """void func()
                {
                    !a[1]||!b[1]&&!c[1];
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            BinaryOp("||",UnaryOp("!",ArrayCell(Id("a"),IntLiteral(1))),BinaryOp("&&",UnaryOp("!",ArrayCell(Id("b"),IntLiteral(1))),UnaryOp("!",ArrayCell(Id("c"),IntLiteral(1)))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_stmt_if(self):
        input = """void func()
                {
                    if (a>b) c = 1;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("c"),IntLiteral(1)),None)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_stmt_if_else(self):
        input = """void func()
                {
                    if (a>b) c = 1;
                    else c = 2;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("c"),IntLiteral(1)),BinaryOp("=",Id("c"),IntLiteral(2)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_stmt_if_else_complex_1(self):
        input = """void func()
                {
                    if(c!=d) d = 1;
                    if (a>b) c = 1;
                    else c = 2;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        If(BinaryOp("!=",Id("c"),Id("d")),BinaryOp("=",Id("d"),IntLiteral(1)),None),
        If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("c"),IntLiteral(1)),BinaryOp("=",Id("c"),IntLiteral(2)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_stmt_if_else_complex_2(self):
        input = """void func()
                {
                    if(c!=d) if (a>b) c = 1;
                    else c = 2;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        If(BinaryOp("!=",Id("c"),Id("d")),If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("c"),IntLiteral(1)),BinaryOp("=",Id("c"),IntLiteral(2))),None)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_stmt_if_else_complex_3(self):
        input = """void func()
                {
                    if(a==1) b = 1;
                    else if (a==2) b = 2;
                    else if (a==3) b = 3;
                    else if (a==4) b = 4;
                    else if (a==5) b = 5;
                    else b = 0;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        If(BinaryOp("==",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(1)),
            If(BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp("=",Id("b"),IntLiteral(2)),
                If(BinaryOp("==",Id("a"),IntLiteral(3)),BinaryOp("=",Id("b"),IntLiteral(3)),
                    If(BinaryOp("==",Id("a"),IntLiteral(4)),BinaryOp("=",Id("b"),IntLiteral(4)),
                        If(BinaryOp("==",Id("a"),IntLiteral(5)),BinaryOp("=",Id("b"),IntLiteral(5)),
                            BinaryOp("=",Id("b"),IntLiteral(0)))))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_stmt_do_while(self):
        input = """void func()
                {
                    do
                    b = 10;
                    a = a + b;
                    while a > b;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        Dowhile([BinaryOp("=",Id("b"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),Id("b")))],BinaryOp(">",Id("a"),Id("b")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_stmt_do_while_complex_1(self):
        input = """void func()
                {
                    do
                    {
                        int c,d;
                        a = a + 1;
                    }
                    b = b - 1;
                    while a > b;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        Dowhile([Block([VarDecl("c",IntType()),VarDecl("d",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]),BinaryOp("=",Id("b"),BinaryOp("-",Id("b"),IntLiteral(1)))],BinaryOp(">",Id("a"),Id("b")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_stmt_do_while_complex_2(self):
        input = """void func()
                {
                    do
                        do
                            do
                                a = a + 1;
                            while a > b;
                            do
                                a = a + 1;
                            while a > b;
                        while a > b;
                        do
                            do
                                a = a + 1;
                            while a > b;
                            do
                                a = a + 1;
                            while a > b;
                        while a > b;
                    while a > b;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([ #Dowhile([],BinaryOp(">",Id("a"),Id("b")))
        Dowhile([Dowhile([Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp(">",Id("a"),Id("b"))),
                          Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp(">",Id("a"),Id("b")))],
                 BinaryOp(">",Id("a"),Id("b"))),
                 Dowhile([Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp(">",Id("a"),Id("b"))),
                          Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp(">",Id("a"),Id("b")))],
                 BinaryOp(">",Id("a"),Id("b")))],
        BinaryOp(">",Id("a"),Id("b")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_stmt_for(self):
        input = """void func()
                {
                    for(i = 1; i < 10; i = i + 1)
                    a = a + 1;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_stmt_for_complex_1(self):
        input = """void func()
                {
                    for(i = 1; i < 10; i = i + 1)
                    {
                        int c,d;
                        a = a + 1;
                    }
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
            Block([VarDecl("c",IntType()),VarDecl("d",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_stmt_for_complex_2(self):
        input = """void func()
                {
                    for(i = 1; i < 10; i = i + 1)
                        for(i = 1; i < 10; i = i + 1)
                            for(i = 1; i < 10; i = i + 1)
                                for(i = 1; i < 10; i = i + 1)
                                    for(i = 1; i < 10; i = i + 1)
                                        a = a + 1;

                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
            For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                    For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                            BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))
            )))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_stmt_break(self):
        input = """void func()
                {
                    for(i = 1; i < 10; i = i + 1)
                    {
                        int c,d;
                        a = a + 1;
                        break;
                    }
                    break;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
            Block([VarDecl("c",IntType()),VarDecl("d",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Break()])),Break()
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_stmt_continue(self):
        input = """void func()
                {
                    for(i = 1; i < 10; i = i + 1)
                    {
                        int c,d;
                        a = a + 1;
                        continue;
                    }
                    continue;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
            Block([VarDecl("c",IntType()),VarDecl("d",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Continue()])),Continue()
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_stmt_return(self):
        input = """void func()
                {
                    for(i = 1; i < 10; i = i + 1)
                    {
                        int c,d;
                        a = a + 1;
                        continue;
                    }
                    return;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
            Block([VarDecl("c",IntType()),VarDecl("d",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Continue()])),Return(None)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_stmt_return_exp(self):
        input = """void func()
                {
                    for(i = 1; i < 10; i = i + 1)
                    {
                        int c,d;
                        a = a + 1;
                        return a + b;
                    }
                    return;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
        For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
            Block([VarDecl("c",IntType()),VarDecl("d",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Return(BinaryOp("+",Id("a"),Id("b")))])),Return(None)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    def test_stmt_block_empty(self):
        input = """void func()
                {
                    {}{}{}
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            Block([]),Block([]),Block([])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_stmt_block_nested(self):
        input = """void func()
                {
                    {{}{}{}}{{}{}{}}{{}{}{}}
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            Block([Block([]),Block([]),Block([])]),Block([Block([]),Block([]),Block([])]),Block([Block([]),Block([]),Block([])])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_stmt_mix_all_simple_1(self):
        input = """void func()
                {
                    if(a==1)
                        for (i = 1; i < 10; i = i + 1)
                            do
                                a = a+1;
                            while a < 10;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            If(BinaryOp("==",Id("a"),IntLiteral(1)),
                For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                    Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("<",Id("a"),IntLiteral(10)))),None)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_stmt_mix_all_simple_2(self):
        input = """void func()
                {
                    if(a==1)
                        for (i = 1; i < 10; i = i + 1)
                            do
                                a = a+1;
                            while a < 10;
                    else
                        for (i = 1; i < 10; i = i + 1)
                            do
                                a = a+1;
                            while a < 10;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            If(BinaryOp("==",Id("a"),IntLiteral(1)),
                For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                    Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("<",Id("a"),IntLiteral(10)))),
                For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                    Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("<",Id("a"),IntLiteral(10)))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_stmt_mix_all_simple_3(self):
        input = """void func()
                {
                    for (i = 1; i < 10; i = i + 1)
                        if(a==1)
                            do
                                a = a+1;
                            while a < 10;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                If(BinaryOp("==",Id("a"),IntLiteral(1)),
                    Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("<",Id("a"),IntLiteral(10))),None))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_stmt_mix_all_simple_4(self):
        input = """void func()
                {
                    for (i = 1; i < 10; i = i + 1)
                        if(a==1)
                            do
                                a = a+1;
                            while a < 10;
                        else
                            do
                                a = a+1;
                            while a < 10;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                If(BinaryOp("==",Id("a"),IntLiteral(1)),
                    Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("<",Id("a"),IntLiteral(10))),
                    Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("<",Id("a"),IntLiteral(10)))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_stmt_mix_all_simple_5(self):
        input = """void func()
                {
                    do
                        a = a+1;
                        if(a==1)
                            for (i = 1; i < 10; i = i + 1)
                                do
                                    a = a+1;
                                while a < 10;
                    while a < 10;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),If(BinaryOp("==",Id("a"),IntLiteral(1)),
                For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                    Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("<",Id("a"),IntLiteral(10)))),None)],BinaryOp("<",Id("a"),IntLiteral(10)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_stmt_mix_all_simple_6(self):
        input = """void func()
                {
                    do
                        a = a+1;
                        if(a==1)
                            for (i = 1; i < 10; i = i + 1)
                                do
                                    a = a+1;
                                while a < 10;
                        else
                            for (i = 1; i < 10; i = i + 1)
                                do
                                    a = a+1;
                                while a < 10;
                    while a < 10;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),If(BinaryOp("==",Id("a"),IntLiteral(1)),
                For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                    Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("<",Id("a"),IntLiteral(10)))),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                    Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BinaryOp("<",Id("a"),IntLiteral(10)))))],BinaryOp("<",Id("a"),IntLiteral(10)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_stmt_mix_all(self):
        input = """void func()
                {
                    if(a==1)
                        for (i = 1; i < 10; i = i + 1)
                            do
                                a = a+1;
                                break;
                                continue;
                                return;
                                return 1;
                            while a < 10;
                    else
                        for (i = 1; i < 10; i = i + 1)
                            do
                                a = a+1;
                                break;
                                continue;
                                return;
                                return 1;
                            while a < 10;
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([
            If(BinaryOp("==",Id("a"),IntLiteral(1)),
                For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                    Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Break(),Continue(),Return(None),Return(IntLiteral(1))],BinaryOp("<",Id("a"),IntLiteral(10)))),
                For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                    Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Break(),Continue(),Return(None),Return(IntLiteral(1))],BinaryOp("<",Id("a"),IntLiteral(10)))),
            )
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_program_super_case_1(self):
        input = """void func()
                {
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_program_super_case_2(self):
        input = """void func()
                {
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_program_super_case_3(self):
        input = """void func()
                {
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_program_super_case_4(self):
        input = """void func()
                {
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_program_super_case_5(self):
        input = """void func()
                {
                }"""
        expect =  str(Program([FuncDecl(Id("func"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
