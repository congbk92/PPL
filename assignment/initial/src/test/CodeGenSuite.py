import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    #Check Literal

    def test_int_lit(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_float_lit(self):
        input = """void main() {
                    putFloat(100.001);
                }"""
        expect = "100.001"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_boolean_lit(self):
        input = """void main() {
                    putBoolLn(true);
                    putBool(false);
                }"""
        expect = "true\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_string_lit(self):
        input = """void main() {
                    putString("This is a string");
                }"""
        expect = "This is a string"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_int_vs_int(self):
        input = """void main() {
                    putInt(10 + 100);
                }"""
        expect = "110"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_float_vs_float(self):
        input = """void main() {
                    putFloat(10.1 + 100.4);
                }"""
        expect = "110.5"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_float_vs_int(self):
        input = """void main() {
                    putFloat(10.1 + 100);
                }"""
        expect = "110.1"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_int_vs_float(self):
        input = """void main() {
                    putFloat(10 + 100.4);
                }"""
        expect = "110.4"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_int_vs_float_complex(self):
        input = """void main() {
                    putFloat(10*10 + 100.4/2 - 15*2.3 + 2.2/1.2 + 5/2);
                }"""
        expect = "119.53333"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_func_decl(self):
        input = """
                int sum_int(int a, int b){
                    return a + b;
                }

                void main() {
                    putInt(sum_int(1001,10));
                }"""
        expect = "1011"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_func_float(self):
        input = """
                float sum_float(float a, float b){
                    return a + b;
                }

                void main() {
                    putFloat(sum_float(1001.1,10.1));
                }"""
        expect = "1011.19995"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_func_pass_float_by_int(self):
        input = """
                int sum_int(int a, int b){
                    return a + b;
                }

                void main() {
                    putFloat(sum_int(1001,10));
                }"""
        expect = "1011.0"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    
    def test_func_pass_float_by_int_1(self):
        input = """
                float sum_float(float a, float b){
                    return a + b;
                }

                void main() {
                    putFloat(sum_float(1001,10));
                }"""
        expect = "1011.0"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_func_return_float_by_int(self):
        input = """
                float sum_float(int a, int b){
                    return a + b;
                }

                void main() {
                    putFloat(sum_float(1001,10));
                }"""
        expect = "1011.0"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_func_using_before_define(self):
        input = """
                void main() {
                    putFloatLn(sum_float(1001,10));
                    {
                        int a;
                        int b;
                        a = 1;
                        b = 2;
                        putInt(a+b);
                    }
                }
                float sum_float(int a, int b){
                    return a + b;
                }
                """
        expect = "1011.0\n3"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_assign_op_simple(self):
        input = """void main() {
                    int a;
                    a = 100;
                    putIntLn(a);
                    float b;
                    b = 1.1;
                    putFloat(b);

                }"""
        expect = "100\n1.1"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_assign_op_int_vs_float(self):
        input = """void main() {
                    float a;
                    a = 100;
                    putFloat(a);
                }"""
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_and_op(self):
        input = """void main() {
                    putBoolLn(false&&false);
                    putBoolLn(true&&false);
                    putBoolLn(false&&true);
                    putBool(true&&true);
                }"""
        expect = "false\nfalse\nfalse\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_or_op(self):
        input = """void main() {
                    putBoolLn(false||false);
                    putBoolLn(true||false);
                    putBoolLn(false||true);
                    putBool(true||true);
                }"""
        expect = "false\ntrue\ntrue\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_or_op_short_circuit(self):
        input = """
                boolean val_true(){
                    putStringLn("val_true");
                    return true;
                }
                boolean val_false(){
                    putStringLn("val_false");
                    return false;
                }
                void main() {
                    boolean a;
                    a = val_true()||val_false();
                }"""
        expect = "val_true\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_or_op_short_circuit_complex(self):
        input = """
                boolean val_true(){
                    putStringLn("val_true");
                    return true;
                }
                boolean val_false(int a){
                    putString("val_false");
                    putInt(a);
                    putLn();
                    return false;
                }
                void main() {
                    boolean a;
                    a = val_false(1)||val_false(2)&&val_true();
                }"""
        expect = "val_false1\nval_false2\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_and_op_short_circuit(self):
        input = """
                boolean val_true(){
                    putStringLn("val_true");
                    return true;
                }
                boolean val_false(){
                    putStringLn("val_false");
                    return false;
                }
                void main() {
                    boolean a;
                    a = val_false()&&val_true();
                }"""
        expect = "val_false\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_and_op_short_circuit_complex(self):
        input = """
                boolean val_true(int a){
                    putString("val_true");
                    putInt(a);
                    putLn();
                    return true;
                }
                boolean val_false(){
                    putStringLn("val_false");
                    return false;
                }
                void main() {
                    boolean a;
                    a = val_true(1)&&(val_true(2)||val_false());
                }"""
        expect = "val_true1\nval_true2\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_boolean_relation_op(self):
        input = """
                void main() {
                    putBoolLn(true==true);
                    putBoolLn(true==false);
                    putBoolLn(false==true);
                    putBoolLn(false==false);

                    putBoolLn(true!=true);
                    putBoolLn(true!=false);
                    putBoolLn(false!=true);
                    putBoolLn(false!=false);
                    {
                        boolean a,b;
                        a = true;
                        b = false;
                        putBoolLn(a&&b==a||b);
                        putBoolLn(a&&b!=a||b);
                    }
                }"""
        expect = "true\nfalse\nfalse\ntrue\nfalse\ntrue\ntrue\nfalse\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_int_relation_op(self):
        input = """
                void main() {
                    putBoolLn(1000==1000);
                    putBoolLn(1212==2212);
                    putBoolLn(1000!=1000);
                    putBoolLn(1212!=2212);

                    putBoolLn(1000>1000);
                    putBoolLn(1212<2212);
                    putBoolLn(1000<=1000);
                    putBoolLn(1212>=2212);

                    {
                        int a,b;
                        a = 1000;
                        b = 2212;
                        putBoolLn(a==b);
                        putBoolLn(a!=b);
                        putBoolLn(a>b==a<=b);
                        putBoolLn(a>=b!=a<b);
                    }

                }"""
        expect = "true\nfalse\nfalse\ntrue\nfalse\ntrue\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_float_relation_op(self):
        input = """
                void main() {
                    putBoolLn(1000.1>1000.1);
                    putBoolLn(1212.2<2212.3);
                    putBoolLn(1000.65<=1000.65);
                    putBoolLn(1212.534>=2212.6542);
                    {
                        float a,b;
                        a = 1000.101;
                        b = 2212.32;
                        putBoolLn(a>=b);
                        putBoolLn(a<=b);
                        putBoolLn(a>b);
                        putBoolLn(a<b);
                    }
                }"""
        expect = "false\ntrue\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_float_vs_int_relation_op(self):
        input = """
                void main() {
                    float a;
                    int b;
                    a = 1000.101;
                    b = 2212;

                    putBoolLn(a>=b);
                    putBoolLn(a<=b);
                    putBoolLn(a>b);
                    putBoolLn(a<b);

                    putBoolLn(b>=a);
                    putBoolLn(b<=a);
                    putBoolLn(b>a);
                    putBoolLn(b<a);

                }"""
        expect = "false\ntrue\nfalse\ntrue\ntrue\nfalse\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_mod_op(self):
        input = """
                void main() {
                    int a,b;
                    a = 39;
                    b = 5;
                    putIntLn(a%b);
                    putIntLn(1024%32);
                }"""
        expect = "4\n0\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_not_op(self):
        input = """
                void main() {
                    boolean a;
                    a = true;
                    putBoolLn(!a);
                    putBoolLn(!!a);
                    putBoolLn(!true);
                    putBoolLn(!false);
                }"""
        expect = "false\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_neg_op(self):
        input = """
                void main() {
                    int a;
                    a = 1;
                    float b;
                    b = 1.123;
                    putIntLn(-a);
                    putIntLn(----a);
                    putFloatLn(-b);
                    putFloatLn(----b);
                }"""
        expect = "-1\n1\n-1.123\n1.123\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_arr_int(self):
        input = """
                void main() {
                    int arr[3];
                    
                    arr[0] = 10;
                    arr[1] = -20;
                    arr[2] = 30;
                    putIntLn(arr[0]);
                    putIntLn(arr[1]);
                    putIntLn(arr[2]);

                }"""
        expect = "10\n-20\n30\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_arr_float(self):
        input = """
                void main() {
                    float arr[3];
                    arr[0] = 10;
                    arr[1] = -20;
                    arr[2] = 30;
                    putFloatLn(arr[0]);
                    putFloatLn(arr[1]);
                    putFloatLn(arr[2]);

                }"""
        expect = "10.0\n-20.0\n30.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_arr_bool(self):
        input = """
                void main() {
                    boolean arr[3];
                    arr[0] = true;
                    arr[1] = !arr[0];
                    arr[2] = arr[0]&&arr[1];
                    putBoolLn(arr[0]);
                    putBoolLn(arr[1]);
                    putBoolLn(arr[2]);

                }"""
        expect = "true\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_arr_string(self):
        input = """
                void main() {
                    string arr[3];
                    arr[0] = "string1";
                    arr[1] = "string2";
                    arr[2] = "string3";
                    putStringLn(arr[0]);
                    putStringLn(arr[1]);
                    putStringLn(arr[2]);

                }"""
        expect = "string1\nstring2\nstring3\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_arr_recusive(self):
        input = """
                void main() {
                    int arr[6];
                    arr[0] = 0;
                    arr[1] = 1;
                    arr[2] = 2;
                    arr[3] = 3;
                    arr[4] = 4;
                    arr[5] = 1005;
                    putIntLn(arr[arr[arr[arr[arr[arr[0] + 1] + 1] + 1] + 1] + 1]);

                }"""
        expect = "1005\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    #To do: add code to set default value for array string
    def test_global_var(self):
        input = """
                void main() {
                    putIntLn(a);
                    putFloatLn(b);
                    putStringLn(c);
                    putBoolLn(d);
                    a = 1;
                    b = 1.1;
                    c = "abc";
                    d = true;
                    putIntLn(a);
                    putFloatLn(b);
                    putStringLn(c);
                    putBoolLn(d);

                    putIntLn(a_arr[3]);
                    putFloatLn(b_arr[3]);
                    putStringLn(c_arr[3]);
                    putBoolLn(d_arr[3]);
                    a_arr[3] = 123;
                    b_arr[3] = 123.123;
                    c_arr[3] = "string3";
                    d_arr[3] = true;
                    putIntLn(a_arr[3]);
                    putFloatLn(b_arr[3]);
                    putStringLn(c_arr[3]);
                    putBoolLn(d_arr[3]);
                }
                int a;
                float b;
                string c;
                boolean d;
                int a_arr[5];
                float b_arr[5];
                string c_arr[5];
                boolean d_arr[5];"""
        expect = "0\n0.0\n\nfalse\n1\n1.1\nabc\ntrue\n0\n0.0\nnull\nfalse\n123\n123.123\nstring3\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_multi_assign_id(self):
        input = """
                void main() {
                    int a,b,c,d;
                    a = 123;
                    b = c = d = a;
                    putIntLn(a);
                    putIntLn(b);
                    putIntLn(c);
                    putIntLn(d);
                }
                """
        expect = "123\n123\n123\n123\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_multi_assign_arr(self):
        input = """
                void main() {
                    int a;
                    int arr[4];
                    arr[1] = 123;
                    arr[0] = arr[3] = a = arr[2] = arr[1];
                    putIntLn(arr[0]);
                    putIntLn(arr[1]);
                    putIntLn(arr[2]);
                    putIntLn(arr[3]);
                    putIntLn(a);
                }
                """
        expect = "123\n123\n123\n123\n123\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))
