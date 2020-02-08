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

    #Test operation for int
    def test_op_for_int_local_var(self):
        input = """
                void main() {
                    int a;
                    a = 2;
                    int b;
                    b = 5;
                    int result;

                    result = a+b;
                    putIntLn(result);
                    result = a-b;
                    putIntLn(result);
                    result = a*b;
                    putIntLn(result);
                    result = b/a;
                    putIntLn(result);
                    result = a+b*a+b/a-a/b;
                    putIntLn(result);

                    boolean rsult;
                    rsult = a+b >= b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a+b >= b-a;
                    putBoolLn(rsult);
                    rsult = a >= b+a;
                    putBoolLn(rsult);
                    rsult = a+b > b-a;
                    putBoolLn(rsult);
                    rsult = a+b > b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a > a+b;
                    putBoolLn(rsult);

                    rsult = a+b <= b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a+b <= b-a;
                    putBoolLn(rsult);
                    rsult = a <= b+a;
                    putBoolLn(rsult);
                    rsult = a+b < b-a;
                    putBoolLn(rsult);
                    rsult = a+b < b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a < a+b;
                    putBoolLn(rsult);

                    putIntLn(b%a);
                    putIntLn(---a);

                    putBoolLn(a==a);
                    putBoolLn(b!=b);
                    putBoolLn(a==b);
                    putBoolLn(b!=a);
                }
                """
        expect = "7\n-3\n10\n2\n14\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n1\n-2\ntrue\nfalse\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_global_var(self):
        input = """
                int a;
                int b;
                int result;
                boolean rsult;
                void main() {
                    a = 2;
                    b = 5;

                    result = a+b;
                    putIntLn(result);
                    result = a-b;
                    putIntLn(result);
                    result = a*b;
                    putIntLn(result);
                    result = b/a;
                    putIntLn(result);
                    result = a+b*a+b/a-a/b;
                    putIntLn(result);

                    rsult = a+b >= b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a+b >= b-a;
                    putBoolLn(rsult);
                    rsult = a >= b+a;
                    putBoolLn(rsult);
                    rsult = a+b > b-a;
                    putBoolLn(rsult);
                    rsult = a+b > b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a > a+b;
                    putBoolLn(rsult);

                    rsult = a+b <= b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a+b <= b-a;
                    putBoolLn(rsult);
                    rsult = a <= b+a;
                    putBoolLn(rsult);
                    rsult = a+b < b-a;
                    putBoolLn(rsult);
                    rsult = a+b < b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a < a+b;
                    putBoolLn(rsult);

                    putIntLn(b%a);
                    putIntLn(---a);

                    putBoolLn(a==a);
                    putBoolLn(b!=b);
                    putBoolLn(a==b);
                    putBoolLn(b!=a);
                }
                """
        expect = "7\n-3\n10\n2\n14\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n1\n-2\ntrue\nfalse\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_pass_func(self):
        input = """
                int a;
                int b;
                int result;
                boolean rsult;

                void func(int a, int b){
                    result = a+b;
                    putIntLn(result);
                    result = a-b;
                    putIntLn(result);
                    result = a*b;
                    putIntLn(result);
                    result = b/a;
                    putIntLn(result);
                    result = a+b*a+b/a-a/b;
                    putIntLn(result);

                    rsult = a+b >= b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a+b >= b-a;
                    putBoolLn(rsult);
                    rsult = a >= b+a;
                    putBoolLn(rsult);
                    rsult = a+b > b-a;
                    putBoolLn(rsult);
                    rsult = a+b > b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a > a+b;
                    putBoolLn(rsult);

                    rsult = a+b <= b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a+b <= b-a;
                    putBoolLn(rsult);
                    rsult = a <= b+a;
                    putBoolLn(rsult);
                    rsult = a+b < b-a;
                    putBoolLn(rsult);
                    rsult = a+b < b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a < a+b;
                    putBoolLn(rsult);

                    putIntLn(b%a);
                    putIntLn(---a);

                    putBoolLn(a==a);
                    putBoolLn(b!=b);
                    putBoolLn(a==b);
                    putBoolLn(b!=a);
                }
                void main() {
                    func(2,5);
                }
                """
        expect = "7\n-3\n10\n2\n14\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n1\n-2\ntrue\nfalse\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_return_from_func(self):
        input = """
                int func_a()
                {
                    return 2;
                }

                int func_b()
                {
                    return 5;
                }

                int func_a1()
                {
                    int arr[1];
                    arr[0] = 2;
                    return arr[0];
                }

                int func_b1()
                {
                    int arr[1];
                    arr[0] = 5;
                    return arr[0];
                }

                void func(int a, int b){
                    int result;
                    boolean rsult;

                    result = func_a()+func_b();
                    putIntLn(result);
                    result = func_a()-func_b();
                    putIntLn(result);
                    result = func_a()*func_b();
                    putIntLn(result);
                    result = func_b()/func_a();
                    putIntLn(result);
                    result = func_a()+func_b()*func_a()+func_b()/func_a()-func_a()/func_b();
                    putIntLn(result);

                    rsult = func_a()+func_b() >= func_b()-func_a()+func_a()+func_a();
                    putBoolLn(rsult);
                    rsult = func_a()+func_b() >= func_b()-func_a();
                    putBoolLn(rsult);
                    rsult = func_a() >= func_b()+func_a();
                    putBoolLn(rsult);
                    rsult = func_a()+func_b() > func_b()-func_a();
                    putBoolLn(rsult);
                    rsult = func_a()+func_b() > func_b()-func_a()+func_a()+func_a();
                    putBoolLn(rsult);
                    rsult = func_a() > func_a()+func_b();
                    putBoolLn(rsult);

                    rsult = func_a1()+func_b1() <= func_b1()-func_a1()+func_a1()+func_a1();
                    putBoolLn(rsult);
                    rsult = func_a1()+func_b1() <= func_b1()-func_a1();
                    putBoolLn(rsult);
                    rsult = func_a1() <= func_b1()+func_a1();
                    putBoolLn(rsult);
                    rsult = func_a1()+func_b1() < func_b1()-func_a1();
                    putBoolLn(rsult);
                    rsult = func_a1()+func_b1() < func_b1()-func_a1()+func_a1()+func_a1();
                    putBoolLn(rsult);
                    rsult = func_a1() < func_a1()+func_b1();
                    putBoolLn(rsult);

                    putIntLn(func_b()%func_a());
                    putIntLn(---func_a());

                    putBoolLn(func_a()==func_a());
                    putBoolLn(func_b()!=func_b());
                    putBoolLn(func_a()==func_b());
                    putBoolLn(func_b()!=func_a());

                }
                void main() {
                    func(2,5);
                }
                """
        expect = "7\n-3\n10\n2\n14\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n1\n-2\ntrue\nfalse\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_local_arr(self):
        input = """
                void main() {
                    int arr[3];
                    arr[0] = 2;
                    arr[2] = 5;
                    int result;
                    boolean rsult;

                    result = arr[0]+arr[2];
                    putIntLn(result);
                    result = arr[0]-arr[2];
                    putIntLn(result);
                    result = arr[0]*arr[2];
                    putIntLn(result);
                    result = arr[2]/arr[0];
                    putIntLn(result);
                    result = arr[0]+arr[2]*arr[0]+arr[2]/arr[0]-arr[0]/arr[2];
                    putIntLn(result);

                    rsult = arr[0]+arr[2] >= arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] >= arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] >= arr[2]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] > arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] > arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] > arr[0]+arr[2];
                    putBoolLn(rsult);

                    rsult = arr[0]+arr[2] <= arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] <= arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] <= arr[2]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] < arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] < arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] < arr[0]+arr[2];
                    putBoolLn(rsult);

                    putIntLn(arr[2]%arr[0]);
                    putIntLn(---arr[0]);

                    putBoolLn(arr[0]==arr[0]);
                    putBoolLn(arr[2]!=arr[2]);
                    putBoolLn(arr[0]==arr[2]);
                    putBoolLn(arr[0]!=arr[2]);

                }
                """
        expect = "7\n-3\n10\n2\n14\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n1\n-2\ntrue\nfalse\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_global_arr(self):
        input = """
                int arr[3];
                boolean rsult;
                int result;
                void main() {
                    arr[0] = 2;
                    arr[2] = 5;

                    result = arr[0]+arr[2];
                    putIntLn(result);
                    result = arr[0]-arr[2];
                    putIntLn(result);
                    result = arr[0]*arr[2];
                    putIntLn(result);
                    result = arr[2]/arr[0];
                    putIntLn(result);
                    result = arr[0]+arr[2]*arr[0]+arr[2]/arr[0]-arr[0]/arr[2];
                    putIntLn(result);

                    rsult = arr[0]+arr[2] >= arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] >= arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] >= arr[2]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] > arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] > arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] > arr[0]+arr[2];
                    putBoolLn(rsult);

                    rsult = arr[0]+arr[2] <= arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] <= arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] <= arr[2]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] < arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] < arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] < arr[0]+arr[2];
                    putBoolLn(rsult);

                    putIntLn(arr[2]%arr[0]);
                    putIntLn(---arr[0]);

                    putBoolLn(arr[0]==arr[0]);
                    putBoolLn(arr[2]!=arr[2]);
                    putBoolLn(arr[0]==arr[2]);
                    putBoolLn(arr[0]!=arr[2]);
                }
                """
        expect = "7\n-3\n10\n2\n14\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n1\n-2\ntrue\nfalse\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_array_pnt_pass_to_func(self):
        input = """
                void func(int arr[]){
                    boolean rsult;
                    int result;

                    result = arr[0]+arr[2];
                    putIntLn(result);
                    result = arr[0]-arr[2];
                    putIntLn(result);
                    result = arr[0]*arr[2];
                    putIntLn(result);
                    result = arr[2]/arr[0];
                    putIntLn(result);
                    result = arr[0]+arr[2]*arr[0]+arr[2]/arr[0]-arr[0]/arr[2];
                    putIntLn(result);

                    rsult = arr[0]+arr[2] >= arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] >= arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] >= arr[2]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] > arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] > arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] > arr[0]+arr[2];
                    putBoolLn(rsult);

                    rsult = arr[0]+arr[2] <= arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] <= arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] <= arr[2]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] < arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] < arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] < arr[0]+arr[2];
                    putBoolLn(rsult);

                    putIntLn(arr[2]%arr[0]);
                    putIntLn(---arr[0]);

                    putBoolLn(arr[0]==arr[0]);
                    putBoolLn(arr[2]!=arr[2]);
                    putBoolLn(arr[0]==arr[2]);
                    putBoolLn(arr[0]!=arr[2]);
                }

                void main() {
                    int arr[3];
                    arr[0] = 2;
                    arr[2] = 5;
                    func(arr);
                }
                """
        expect = "7\n-3\n10\n2\n14\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n1\n-2\ntrue\nfalse\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_array_pnt_return_from_func(self):
        input = """
                int[] func(int arr[]){
                    arr[0] = 2;
                    arr[2] = 5;
                    return arr;
                }

                void main() {
                    int arr[3];
                    boolean rsult;
                    int result;

                    result = func(arr)[0]+func(arr)[2];
                    putIntLn(result);
                    result = func(arr)[0]-func(arr)[2];
                    putIntLn(result);
                    result = func(arr)[0]*func(arr)[2];
                    putIntLn(result);
                    result = func(arr)[2]/func(arr)[0];
                    putIntLn(result);
                    result = func(arr)[0]+func(arr)[2]*func(arr)[0]+func(arr)[2]/func(arr)[0]-func(arr)[0]/func(arr)[2];
                    putIntLn(result);

                    rsult = func(arr)[0]+func(arr)[2] >= func(arr)[2]-func(arr)[0]+func(arr)[0]+func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0]+func(arr)[2] >= func(arr)[2]-func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0] >= func(arr)[2]+func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0]+func(arr)[2] > func(arr)[2]-func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0]+func(arr)[2] > func(arr)[2]-func(arr)[0]+func(arr)[0]+func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0] > func(arr)[0]+func(arr)[2];
                    putBoolLn(rsult);

                    rsult = func(arr)[0]+func(arr)[2] <= func(arr)[2]-func(arr)[0]+func(arr)[0]+func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0]+func(arr)[2] <= func(arr)[2]-func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0] <= func(arr)[2]+func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0]+func(arr)[2] < func(arr)[2]-func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0]+func(arr)[2] < func(arr)[2]-func(arr)[0]+func(arr)[0]+func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0] < func(arr)[0]+func(arr)[2];
                    putBoolLn(rsult);

                    putIntLn(func(arr)[2]%func(arr)[0]);
                    putIntLn(---func(arr)[0]);

                    putBoolLn(func(arr)[0]==func(arr)[0]);
                    putBoolLn(func(arr)[2]!=func(arr)[2]);
                    putBoolLn(func(arr)[0]==func(arr)[2]);
                    putBoolLn(func(arr)[0]!=func(arr)[2]);
                }
                """
        expect = "7\n-3\n10\n2\n14\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n1\n-2\ntrue\nfalse\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    #Test operation for float

    def test_op_for_float_local_var(self):
        input = """
                void main() {
                    float a;
                    a = 2.5;
                    float b;
                    b = 5.7;
                    float result;

                    result = a+b;
                    putFloatLn(result);
                    result = a-b;
                    putFloatLn(result);
                    result = a*b;
                    putFloatLn(result);
                    result = b/a;
                    putFloatLn(result);
                    result = a+b*a+b/a-a/b;
                    putFloatLn(result);

                    boolean rsult;
                    rsult = a+b >= b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a+b >= b-a;
                    putBoolLn(rsult);
                    rsult = a >= b+a;
                    putBoolLn(rsult);
                    rsult = a+b > b-a;
                    putBoolLn(rsult);
                    rsult = a+b > b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a > a+b;
                    putBoolLn(rsult);

                    rsult = a+b <= b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a+b <= b-a;
                    putBoolLn(rsult);
                    rsult = a <= b+a;
                    putBoolLn(rsult);
                    rsult = a+b < b-a;
                    putBoolLn(rsult);
                    rsult = a+b < b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a < a+b;
                    putBoolLn(rsult);

                    putFloatLn(---a);
                }
                """
        expect = "8.2\n-3.1999998\n14.25\n2.28\n18.591404\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-2.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    
    def test_op_for_float_global_var(self):
        input = """
                float a;
                float b;
                float result;
                boolean rsult;
                void main() {
                    a = 2.5;
                    b = 5.7;

                    result = a+b;
                    putFloatLn(result);
                    result = a-b;
                    putFloatLn(result);
                    result = a*b;
                    putFloatLn(result);
                    result = b/a;
                    putFloatLn(result);
                    result = a+b*a+b/a-a/b;
                    putFloatLn(result);

                    rsult = a+b >= b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a+b >= b-a;
                    putBoolLn(rsult);
                    rsult = a >= b+a;
                    putBoolLn(rsult);
                    rsult = a+b > b-a;
                    putBoolLn(rsult);
                    rsult = a+b > b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a > a+b;
                    putBoolLn(rsult);

                    rsult = a+b <= b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a+b <= b-a;
                    putBoolLn(rsult);
                    rsult = a <= b+a;
                    putBoolLn(rsult);
                    rsult = a+b < b-a;
                    putBoolLn(rsult);
                    rsult = a+b < b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a < a+b;
                    putBoolLn(rsult);
                    
                    putFloatLn(---a);
                }
                """
        expect = "8.2\n-3.1999998\n14.25\n2.28\n18.591404\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-2.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_float_pass_func(self):
        input = """
                float a;
                float b;
                float result;
                boolean rsult;

                void func(float a, float b){
                    result = a+b;
                    putFloatLn(result);
                    result = a-b;
                    putFloatLn(result);
                    result = a*b;
                    putFloatLn(result);
                    result = b/a;
                    putFloatLn(result);
                    result = a+b*a+b/a-a/b;
                    putFloatLn(result);

                    rsult = a+b >= b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a+b >= b-a;
                    putBoolLn(rsult);
                    rsult = a >= b+a;
                    putBoolLn(rsult);
                    rsult = a+b > b-a;
                    putBoolLn(rsult);
                    rsult = a+b > b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a > a+b;
                    putBoolLn(rsult);

                    rsult = a+b <= b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a+b <= b-a;
                    putBoolLn(rsult);
                    rsult = a <= b+a;
                    putBoolLn(rsult);
                    rsult = a+b < b-a;
                    putBoolLn(rsult);
                    rsult = a+b < b-a+a+a;
                    putBoolLn(rsult);
                    rsult = a < a+b;
                    putBoolLn(rsult);

                    putFloatLn(---a);
                }
                void main() {
                    func(2.5,5.7);
                }
                """
        expect = "8.2\n-3.1999998\n14.25\n2.28\n18.591404\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-2.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_float_return_from_func(self):
        input = """
                float func_a()
                {
                    return 2.5;
                }

                float func_b()
                {
                    return 5.7;
                }

                float func_a1()
                {
                    float arr[1];
                    arr[0] = 2.5;
                    return arr[0];
                }

                float func_b1()
                {
                    float arr[1];
                    arr[0] = 5.7;
                    return arr[0];
                }

                void func(int a, int b){
                    float result;
                    boolean rsult;

                    result = func_a()+func_b();
                    putFloatLn(result);
                    result = func_a()-func_b();
                    putFloatLn(result);
                    result = func_a()*func_b();
                    putFloatLn(result);
                    result = func_b()/func_a();
                    putFloatLn(result);
                    result = func_a()+func_b()*func_a()+func_b()/func_a()-func_a()/func_b();
                    putFloatLn(result);

                    rsult = func_a()+func_b() >= func_b()-func_a()+func_a()+func_a();
                    putBoolLn(rsult);
                    rsult = func_a()+func_b() >= func_b()-func_a();
                    putBoolLn(rsult);
                    rsult = func_a() >= func_b()+func_a();
                    putBoolLn(rsult);
                    rsult = func_a()+func_b() > func_b()-func_a();
                    putBoolLn(rsult);
                    rsult = func_a()+func_b() > func_b()-func_a()+func_a()+func_a();
                    putBoolLn(rsult);
                    rsult = func_a() > func_a()+func_b();
                    putBoolLn(rsult);

                    rsult = func_a1()+func_b1() <= func_b1()-func_a1()+func_a1()+func_a1();
                    putBoolLn(rsult);
                    rsult = func_a1()+func_b1() <= func_b1()-func_a1();
                    putBoolLn(rsult);
                    rsult = func_a1() <= func_b1()+func_a1();
                    putBoolLn(rsult);
                    rsult = func_a1()+func_b1() < func_b1()-func_a1();
                    putBoolLn(rsult);
                    rsult = func_a1()+func_b1() < func_b1()-func_a1()+func_a1()+func_a1();
                    putBoolLn(rsult);
                    rsult = func_a1() < func_a1()+func_b1();
                    putBoolLn(rsult);

                    putFloatLn(---func_a());
                }
                void main() {
                    func(2,5);
                }
                """
        expect = "8.2\n-3.1999998\n14.25\n2.28\n18.591404\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-2.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_float_local_arr(self):
        input = """
                void main() {
                    float arr[3];
                    arr[0] = 2.5;
                    arr[2] = 5.7;
                    float result;
                    boolean rsult;

                    result = arr[0]+arr[2];
                    putFloatLn(result);
                    result = arr[0]-arr[2];
                    putFloatLn(result);
                    result = arr[0]*arr[2];
                    putFloatLn(result);
                    result = arr[2]/arr[0];
                    putFloatLn(result);
                    result = arr[0]+arr[2]*arr[0]+arr[2]/arr[0]-arr[0]/arr[2];
                    putFloatLn(result);

                    rsult = arr[0]+arr[2] >= arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] >= arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] >= arr[2]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] > arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] > arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] > arr[0]+arr[2];
                    putBoolLn(rsult);

                    rsult = arr[0]+arr[2] <= arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] <= arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] <= arr[2]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] < arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] < arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] < arr[0]+arr[2];
                    putBoolLn(rsult);

                    putFloatLn(---arr[0]);
                }
                """
        expect = "8.2\n-3.1999998\n14.25\n2.28\n18.591404\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-2.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_float_global_arr(self):
        input = """
                float arr[3];
                boolean rsult;
                float result;
                void main() {
                    arr[0] = 2.5;
                    arr[2] = 5.7;

                    result = arr[0]+arr[2];
                    putFloatLn(result);
                    result = arr[0]-arr[2];
                    putFloatLn(result);
                    result = arr[0]*arr[2];
                    putFloatLn(result);
                    result = arr[2]/arr[0];
                    putFloatLn(result);
                    result = arr[0]+arr[2]*arr[0]+arr[2]/arr[0]-arr[0]/arr[2];
                    putFloatLn(result);

                    rsult = arr[0]+arr[2] >= arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] >= arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] >= arr[2]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] > arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] > arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] > arr[0]+arr[2];
                    putBoolLn(rsult);

                    rsult = arr[0]+arr[2] <= arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] <= arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] <= arr[2]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] < arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] < arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] < arr[0]+arr[2];
                    putBoolLn(rsult);
                    
                    putFloatLn(---arr[0]);
                }
                """
        expect = "8.2\n-3.1999998\n14.25\n2.28\n18.591404\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-2.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_float_array_pnt_pass_to_func(self):
        input = """
                void func(float arr[]){
                    boolean rsult;
                    float result;

                    result = arr[0]+arr[2];
                    putFloatLn(result);
                    result = arr[0]-arr[2];
                    putFloatLn(result);
                    result = arr[0]*arr[2];
                    putFloatLn(result);
                    result = arr[2]/arr[0];
                    putFloatLn(result);
                    result = arr[0]+arr[2]*arr[0]+arr[2]/arr[0]-arr[0]/arr[2];
                    putFloatLn(result);

                    rsult = arr[0]+arr[2] >= arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] >= arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] >= arr[2]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] > arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] > arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] > arr[0]+arr[2];
                    putBoolLn(rsult);

                    rsult = arr[0]+arr[2] <= arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] <= arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] <= arr[2]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] < arr[2]-arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0]+arr[2] < arr[2]-arr[0]+arr[0]+arr[0];
                    putBoolLn(rsult);
                    rsult = arr[0] < arr[0]+arr[2];
                    putBoolLn(rsult);

                    putFloatLn(---arr[0]);
                }

                void main() {
                    float arr[3];
                    arr[0] = 2.5;
                    arr[2] = 5.7;
                    func(arr);
                }
                """
        expect = "8.2\n-3.1999998\n14.25\n2.28\n18.591404\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-2.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_float_array_pnt_return_from_func(self):
        input = """
                float[] func(float arr[]){
                    arr[0] = 2.5;
                    arr[2] = 5.7;
                    return arr;
                }

                void main() {
                    float arr[3];
                    boolean rsult;
                    float result;

                    result = func(arr)[0]+func(arr)[2];
                    putFloatLn(result);
                    result = func(arr)[0]-func(arr)[2];
                    putFloatLn(result);
                    result = func(arr)[0]*func(arr)[2];
                    putFloatLn(result);
                    result = func(arr)[2]/func(arr)[0];
                    putFloatLn(result);
                    result = func(arr)[0]+func(arr)[2]*func(arr)[0]+func(arr)[2]/func(arr)[0]-func(arr)[0]/func(arr)[2];
                    putFloatLn(result);

                    rsult = func(arr)[0]+func(arr)[2] >= func(arr)[2]-func(arr)[0]+func(arr)[0]+func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0]+func(arr)[2] >= func(arr)[2]-func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0] >= func(arr)[2]+func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0]+func(arr)[2] > func(arr)[2]-func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0]+func(arr)[2] > func(arr)[2]-func(arr)[0]+func(arr)[0]+func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0] > func(arr)[0]+func(arr)[2];
                    putBoolLn(rsult);

                    rsult = func(arr)[0]+func(arr)[2] <= func(arr)[2]-func(arr)[0]+func(arr)[0]+func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0]+func(arr)[2] <= func(arr)[2]-func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0] <= func(arr)[2]+func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0]+func(arr)[2] < func(arr)[2]-func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0]+func(arr)[2] < func(arr)[2]-func(arr)[0]+func(arr)[0]+func(arr)[0];
                    putBoolLn(rsult);
                    rsult = func(arr)[0] < func(arr)[0]+func(arr)[2];
                    putBoolLn(rsult);

                    putFloatLn(---func(arr)[0]);
                }
                """
        expect = "8.2\n-3.1999998\n14.25\n2.28\n18.591404\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-2.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    #Test operation for boolean

    def test_op_for_boolean_local_var(self):
        input = """
                void main(){
                    boolean a,b;
                    a = true;
                    b = false;

                    putBoolLn(a&&b);
                    putBoolLn(a||b);
                    putBoolLn(a!=b);
                    putBoolLn(a==b);
                    putBoolLn(!!!a);

                    boolean result;
                    result = (!a&&!b)==(!a||!b);
                    putBoolLn(result);
                    result = (!a&&!b)!=(!a||!b);
                    putBoolLn(result);

                    result = !a==!b&&!a!=!b;
                    putBoolLn(result);
                    result = !a==!b||!a!=!b;
                    putBoolLn(result);
                }
                """
        expect = "false\ntrue\ntrue\nfalse\nfalse\nfalse\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_boolean_global_var(self):
        input = """
                void main(){
                    a = true;
                    b = false;

                    putBoolLn(a&&b);
                    putBoolLn(a||b);
                    putBoolLn(a!=b);
                    putBoolLn(a==b);
                    putBoolLn(!!!a);

                    result = (!a&&!b)==(!a||!b);
                    putBoolLn(result);
                    result = (!a&&!b)!=(!a||!b);
                    putBoolLn(result);

                    result = !a==!b&&!a!=!b;
                    putBoolLn(result);
                    result = !a==!b||!a!=!b;
                    putBoolLn(result);
                }
                boolean result;
                boolean a,b;
                """
        expect = "false\ntrue\ntrue\nfalse\nfalse\nfalse\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_boolean_pass_func(self):
        input = """
                void func(boolean a, boolean b){
                    putBoolLn(a&&b);
                    putBoolLn(a||b);
                    putBoolLn(a!=b);
                    putBoolLn(a==b);
                    putBoolLn(!!!a);

                    result = (!a&&!b)==(!a||!b);
                    putBoolLn(result);
                    result = (!a&&!b)!=(!a||!b);
                    putBoolLn(result);

                    result = !a==!b&&!a!=!b;
                    putBoolLn(result);
                    result = !a==!b||!a!=!b;
                    putBoolLn(result);
                }
                void main(){
                    a = true;
                    b = false;
                    func(a,b);
                }
                boolean result;
                boolean a,b;
                """
        expect = "false\ntrue\ntrue\nfalse\nfalse\nfalse\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_boolean_return_from_func(self):
        input = """
                boolean func_a(){
                    return true;
                }
                boolean func_b(){
                    return false;
                }

                boolean func_a1(boolean a[]){
                    return a[0];
                }
                boolean func_b1(boolean b[]){
                    return b[1];
                }

                void func(boolean a, boolean b){
                    putBoolLn(a&&b);
                    putBoolLn(a||b);
                    putBoolLn(a!=b);
                    putBoolLn(a==b);
                    putBoolLn(!!!a);

                    result = (!func_a()&&!func_b())==(!func_a()||!func_b());
                    putBoolLn(result);
                    result = (!func_a()&&!func_b())!=(!func_a()||!func_b());
                    putBoolLn(result);

                    boolean arr[2];
                    arr[0] = true;
                    arr[1] = false;

                    result = !func_a1(arr)==!func_b1(arr)&&!func_a1(arr)!=!func_b1(arr);
                    putBoolLn(result);
                    result = !func_a1(arr)==!func_b1(arr)||!func_a1(arr)!=!func_b1(arr);
                    putBoolLn(result);
                }
                void main(){
                    a = true;
                    b = false;
                    func(a,b);
                }
                boolean result;
                boolean a,b;
                """
        expect = "false\ntrue\ntrue\nfalse\nfalse\nfalse\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_boolean_local_arr(self):
        input = """
                void main(){
                    boolean a[1],b[1];
                    boolean result;
                    a[0] = true;
                    b[0] = false;

                    putBoolLn(a[0]&&b[0]);
                    putBoolLn(a[0]||b[0]);
                    putBoolLn(a[0]!=b[0]);
                    putBoolLn(a[0]==b[0]);
                    putBoolLn(!!!a[0]);

                    result = (!a[0]&&!b[0])==(!a[0]||!b[0]);
                    putBoolLn(result);
                    result = (!a[0]&&!b[0])!=(!a[0]||!b[0]);
                    putBoolLn(result);

                    result = !a[0]==!b[0]&&!a[0]!=!b[0];
                    putBoolLn(result);
                    result = !a[0]==!b[0]||!a[0]!=!b[0];
                    putBoolLn(result);
                }
                """
        expect = "false\ntrue\ntrue\nfalse\nfalse\nfalse\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_boolean_global_arr(self):
        input = """
                boolean a[1],b[1];
                boolean result;

                void set_value(){
                    a[0] = true;
                    b[0] = false;
                }
                void main(){
                    set_value();

                    putBoolLn(a[0]&&b[0]);
                    putBoolLn(a[0]||b[0]);
                    putBoolLn(a[0]!=b[0]);
                    putBoolLn(a[0]==b[0]);
                    putBoolLn(!!!a[0]);

                    result = (!a[0]&&!b[0])==(!a[0]||!b[0]);
                    putBoolLn(result);
                    result = (!a[0]&&!b[0])!=(!a[0]||!b[0]);
                    putBoolLn(result);

                    result = !a[0]==!b[0]&&!a[0]!=!b[0];
                    putBoolLn(result);
                    result = !a[0]==!b[0]||!a[0]!=!b[0];
                    putBoolLn(result);
                }
                """
        expect = "false\ntrue\ntrue\nfalse\nfalse\nfalse\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_boolean_array_pnt_pass_to_func(self):
        input = """
                boolean a[1],b[1];
                boolean result;

                void func(boolean a[], boolean b[]){
                    putBoolLn(a[0]&&b[0]);
                    putBoolLn(a[0]||b[0]);
                    putBoolLn(a[0]!=b[0]);
                    putBoolLn(a[0]==b[0]);
                    putBoolLn(!!!a[0]);

                    result = (!a[0]&&!b[0])==(!a[0]||!b[0]);
                    putBoolLn(result);
                    result = (!a[0]&&!b[0])!=(!a[0]||!b[0]);
                    putBoolLn(result);

                    result = !a[0]==!b[0]&&!a[0]!=!b[0];
                    putBoolLn(result);
                    result = !a[0]==!b[0]||!a[0]!=!b[0];
                    putBoolLn(result);
                }

                void main(){
                    a[0] = true;
                    b[0] = false;
                    func(a,b);
                }
                """
        expect = "false\ntrue\ntrue\nfalse\nfalse\nfalse\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    
    def test_op_for_boolean_array_pnt_return_from_func(self):
        input = """
                boolean[] func(boolean a[]){
                    return a;
                }

                void main(){
                    boolean a[1],b[1];
                    boolean result;
                    a[0] = true;
                    b[0] = false;
                    

                    putBoolLn(func(a)[0]&&func(b)[0]);
                    putBoolLn(func(a)[0]||func(b)[0]);
                    putBoolLn(func(a)[0]!=func(b)[0]);
                    putBoolLn(func(a)[0]==func(b)[0]);
                    putBoolLn(!!!func(a)[0]);

                    result = (!func(a)[0]&&!func(b)[0])==(!func(a)[0]||!func(b)[0]);
                    putBoolLn(result);
                    result = (!func(a)[0]&&!func(b)[0])!=(!func(a)[0]||!func(b)[0]);
                    putBoolLn(result);

                    result = !func(a)[0]==!func(b)[0]&&!func(a)[0]!=!func(b)[0];
                    putBoolLn(result);
                    result = !func(a)[0]==!func(b)[0]||!func(a)[0]!=!func(b)[0];
                    putBoolLn(result);
                }
                """
        expect = "false\ntrue\ntrue\nfalse\nfalse\nfalse\ntrue\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    #Test operation for string
    def test_op_for_string_local_var(self):
        input = """
                void main(){
                    string a;
                    a = "This is a String";
                    putString(a);
                }
                """
        expect = "This is a String"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_string_global_var(self):
        input = """
                void main(){
                    a = "This is a String";
                    putString(a);
                }
                string a;
                """
        expect = "This is a String"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_string_pass_func(self):
        input = """
                void func(string a){
                    putString(a);
                }
                void main(){
                    a = "This is a String";
                    func(a);
                }
                string a;
                """
        expect = "This is a String"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_string_return_from_func(self):
        input = """
                string func(){
                    return "This is a String";
                }
                string [] func_arr_pnt(string a[]){
                    return a;
                }

                void main(){
                    string a[100];
                    a[0] = "This is a String";
                    putStringLn(func());
                    putString(func_arr_pnt(a)[0]);
                }
                """
        expect = "This is a String\nThis is a String"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_string_local_arr(self):
        input = """
                void main(){
                    string a[3];
                    a[1] = "This is a String";
                    putString(a[1]);
                }
                
                """
        expect = "This is a String"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_string_global_arr(self):
        input = """
                void main(){
                    a[1] = "This is a String";
                    putString(a[1]);
                }
                string a[3];
                """
        expect = "This is a String"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_string_array_pnt_pass_to_func(self):
        input = """
                void func(string arr[]){
                    putString(arr[1]);
                }
                void main(){
                    a[1] = "This is a String";
                    func(a);
                }
                string a[3];
                """
        expect = "This is a String"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_string_array_pnt_return_from_func(self):
        input = """
                string [] func(string arr[]){
                    return arr;
                }
                void main(){
                    a[1] = "This is a String";
                    putString(func(a)[1]);
                }
                string a[3];
                """
        expect = "This is a String"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    #Test operation for int vs float
    def test_op_for_int_vs_float_local_var(self):
        input = """
                void main(){
                    int a;
                    float b;
                    a = 2;
                    b = 5.1;

                    putFloatLn(a+b);
                    putFloatLn(a-b);
                    putFloatLn(a*b);
                    putFloatLn(b/a);
                    putFloatLn(a+b*a+b/a-a/b);

                    putBoolLn(a+b >= b-a+a+a);
                    putBoolLn(a+b >= b-a);
                    putBoolLn(a >= b+a);
                    putBoolLn(a+b > b-a);
                    putBoolLn(a+b > b-a+a+a);
                    putBoolLn(a > a+b);


                    putBoolLn(a+b <= b-a+a+a);
                    putBoolLn(a+b <= b-a);
                    putBoolLn(a <= b+a);
                    putBoolLn(a+b < b-a);
                    putBoolLn(a+b < b-a+a+a);
                    putBoolLn(a < a+b);

                    putFloatLn(-(a+b));
                }
                """
        expect = "7.1\n-3.1\n10.2\n2.55\n14.357843\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-7.1\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_vs_float_global_var(self):
        input = """
                void main(){
                    a = 2;
                    b = 5.1;

                    putFloatLn(a+b);
                    putFloatLn(a-b);
                    putFloatLn(a*b);
                    putFloatLn(b/a);
                    putFloatLn(a+b*a+b/a-a/b);

                    putBoolLn(a+b >= b-a+a+a);
                    putBoolLn(a+b >= b-a);
                    putBoolLn(a >= b+a);
                    putBoolLn(a+b > b-a);
                    putBoolLn(a+b > b-a+a+a);
                    putBoolLn(a > a+b);


                    putBoolLn(a+b <= b-a+a+a);
                    putBoolLn(a+b <= b-a);
                    putBoolLn(a <= b+a);
                    putBoolLn(a+b < b-a);
                    putBoolLn(a+b < b-a+a+a);
                    putBoolLn(a < a+b);

                    putFloatLn(-(a+b));
                }

                int a;
                float b;
                """
        expect = "7.1\n-3.1\n10.2\n2.55\n14.357843\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-7.1\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_vs_float_global_var(self):
        input = """
                void main(){
                    a = 2;
                    b = 5.1;

                    putFloatLn(a+b);
                    putFloatLn(a-b);
                    putFloatLn(a*b);
                    putFloatLn(b/a);
                    putFloatLn(a+b*a+b/a-a/b);

                    putBoolLn(a+b >= b-a+a+a);
                    putBoolLn(a+b >= b-a);
                    putBoolLn(a >= b+a);
                    putBoolLn(a+b > b-a);
                    putBoolLn(a+b > b-a+a+a);
                    putBoolLn(a > a+b);


                    putBoolLn(a+b <= b-a+a+a);
                    putBoolLn(a+b <= b-a);
                    putBoolLn(a <= b+a);
                    putBoolLn(a+b < b-a);
                    putBoolLn(a+b < b-a+a+a);
                    putBoolLn(a < a+b);

                    putFloatLn(-(a+b));
                }

                int a;
                float b;
                """
        expect = "7.1\n-3.1\n10.2\n2.55\n14.357843\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-7.1\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_vs_float_pass_func(self):
        input = """
                void func(float a, float b)
                {
                    putFloatLn(a+b);
                    putFloatLn(a-b);
                    putFloatLn(a*b);
                    putFloatLn(b/a);
                    putFloatLn(a+b*a+b/a-a/b);

                    putBoolLn(a+b >= b-a+a+a);
                    putBoolLn(a+b >= b-a);
                    putBoolLn(a >= b+a);
                    putBoolLn(a+b > b-a);
                    putBoolLn(a+b > b-a+a+a);
                    putBoolLn(a > a+b);


                    putBoolLn(a+b <= b-a+a+a);
                    putBoolLn(a+b <= b-a);
                    putBoolLn(a <= b+a);
                    putBoolLn(a+b < b-a);
                    putBoolLn(a+b < b-a+a+a);
                    putBoolLn(a < a+b);

                    putFloatLn(-(a+b));
                }
                void main(){
                    a = 2;
                    b = 5.1;
                    func(a,b);
                }

                int a;
                float b;
                """
        expect = "7.1\n-3.1\n10.2\n2.55\n14.357843\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-7.1\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_vs_float_return_from_func(self):
        input = """
                int func_a(int a){
                    return a;
                }
                float func_b(float a){
                    return a;
                }
                void func(int a, float b)
                {
                    putFloatLn(func_a(a)+func_b(b));
                    putFloatLn(func_a(a)-func_b(b));
                    putFloatLn(func_a(a)*func_b(b));
                    putFloatLn(func_b(b)/func_a(a));
                    putFloatLn(func_a(a)+func_b(b)*func_a(a)+func_b(b)/func_a(a)-func_a(a)/func_b(b));

                    putBoolLn(func_a(a)+func_b(b) >= func_b(b)-func_a(a)+func_a(a)+func_a(a));
                    putBoolLn(func_a(a)+func_b(b) >= func_b(b)-func_a(a));
                    putBoolLn(func_a(a) >= func_b(b)+func_a(a));
                    putBoolLn(func_a(a)+func_b(b) > func_b(b)-func_a(a));
                    putBoolLn(func_a(a)+func_b(b) > func_b(b)-func_a(a)+func_a(a)+func_a(a));
                    putBoolLn(func_a(a) > func_a(a)+func_b(b));

                    putBoolLn(func_a(a)+func_b(b) <= func_b(b)-func_a(a)+func_a(a)+func_a(a));
                    putBoolLn(func_a(a)+func_b(b) <= func_b(b)-func_a(a));
                    putBoolLn(func_a(a) <= func_b(b)+func_a(a));
                    putBoolLn(func_a(a)+func_b(b) < func_b(b)-func_a(a));
                    putBoolLn(func_a(a)+func_b(b) < func_b(b)-func_a(a)+func_a(a)+func_a(a));
                    putBoolLn(func_a(a) < func_a(a)+func_b(b));

                    putFloatLn(-(func_a(a)+func_b(b)));
                }
                void main(){
                    a = 2;
                    b = 5.1;
                    func(a,b);
                }

                int a;
                float b;
                """
        expect = "7.1\n-3.1\n10.2\n2.55\n14.357843\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-7.1\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_vs_float_local_arr(self):
        input = """
                void main(){
                    int a[10];
                    float b[10];
                    a[5] = 2;
                    b[5] = 5.1;

                    putFloatLn(a[5]+b[5]);
                    putFloatLn(a[5]-b[5]);
                    putFloatLn(a[5]*b[5]);
                    putFloatLn(b[5]/a[5]);
                    putFloatLn(a[5]+b[5]*a[5]+b[5]/a[5]-a[5]/b[5]);

                    putBoolLn(a[5]+b[5] >= b[5]-a[5]+a[5]+a[5]);
                    putBoolLn(a[5]+b[5] >= b[5]-a[5]);
                    putBoolLn(a[5] >= b[5]+a[5]);
                    putBoolLn(a[5]+b[5] > b[5]-a[5]);
                    putBoolLn(a[5]+b[5] > b[5]-a[5]+a[5]+a[5]);
                    putBoolLn(a[5] > a[5]+b[5]);

                    putBoolLn(a[5]+b[5] <= b[5]-a[5]+a[5]+a[5]);
                    putBoolLn(a[5]+b[5] <= b[5]-a[5]);
                    putBoolLn(a[5] <= b[5]+a[5]);
                    putBoolLn(a[5]+b[5] < b[5]-a[5]);
                    putBoolLn(a[5]+b[5] < b[5]-a[5]+a[5]+a[5]);
                    putBoolLn(a[5] < a[5]+b[5]);

                    putFloatLn(-(a[5]+b[5]));
                }
                """
        expect = "7.1\n-3.1\n10.2\n2.55\n14.357843\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-7.1\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_vs_float_global_arr(self):
        input = """
                int a[10];
                float b[10];
                void main(){
                    a[5] = 2;
                    b[5] = 5.1;

                    putFloatLn(a[5]+b[5]);
                    putFloatLn(a[5]-b[5]);
                    putFloatLn(a[5]*b[5]);
                    putFloatLn(b[5]/a[5]);
                    putFloatLn(a[5]+b[5]*a[5]+b[5]/a[5]-a[5]/b[5]);

                    putBoolLn(a[5]+b[5] >= b[5]-a[5]+a[5]+a[5]);
                    putBoolLn(a[5]+b[5] >= b[5]-a[5]);
                    putBoolLn(a[5] >= b[5]+a[5]);
                    putBoolLn(a[5]+b[5] > b[5]-a[5]);
                    putBoolLn(a[5]+b[5] > b[5]-a[5]+a[5]+a[5]);
                    putBoolLn(a[5] > a[5]+b[5]);

                    putBoolLn(a[5]+b[5] <= b[5]-a[5]+a[5]+a[5]);
                    putBoolLn(a[5]+b[5] <= b[5]-a[5]);
                    putBoolLn(a[5] <= b[5]+a[5]);
                    putBoolLn(a[5]+b[5] < b[5]-a[5]);
                    putBoolLn(a[5]+b[5] < b[5]-a[5]+a[5]+a[5]);
                    putBoolLn(a[5] < a[5]+b[5]);

                    putFloatLn(-(a[5]+b[5]));
                }
                """
        expect = "7.1\n-3.1\n10.2\n2.55\n14.357843\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-7.1\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_vs_float_array_pnt_pass_to_func(self):
        input = """
                int a[10];
                float b[10];

                void func(int a[], float b[]){
                    putFloatLn(a[5]+b[5]);
                    putFloatLn(a[5]-b[5]);
                    putFloatLn(a[5]*b[5]);
                    putFloatLn(b[5]/a[5]);
                    putFloatLn(a[5]+b[5]*a[5]+b[5]/a[5]-a[5]/b[5]);

                    putBoolLn(a[5]+b[5] >= b[5]-a[5]+a[5]+a[5]);
                    putBoolLn(a[5]+b[5] >= b[5]-a[5]);
                    putBoolLn(a[5] >= b[5]+a[5]);
                    putBoolLn(a[5]+b[5] > b[5]-a[5]);
                    putBoolLn(a[5]+b[5] > b[5]-a[5]+a[5]+a[5]);
                    putBoolLn(a[5] > a[5]+b[5]);

                    putBoolLn(a[5]+b[5] <= b[5]-a[5]+a[5]+a[5]);
                    putBoolLn(a[5]+b[5] <= b[5]-a[5]);
                    putBoolLn(a[5] <= b[5]+a[5]);
                    putBoolLn(a[5]+b[5] < b[5]-a[5]);
                    putBoolLn(a[5]+b[5] < b[5]-a[5]+a[5]+a[5]);
                    putBoolLn(a[5] < a[5]+b[5]);

                    putFloatLn(-(a[5]+b[5]));
                }
                void main(){
                    a[5] = 2;
                    b[5] = 5.1;
                    func(a,b);
                }
                """
        expect = "7.1\n-3.1\n10.2\n2.55\n14.357843\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-7.1\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_op_for_int_vs_float_array_pnt_return_from_func(self):
        input = """
                int a[10];
                float b[10];

                int[] func_a(int a[]){
                    return a;
                }

                float[] func_b(float a[]){
                    return a;
                }

                void func(int a[], float b[]){
                    putFloatLn(func_a(a)[5]+func_b(b)[5]);
                    putFloatLn(func_a(a)[5]-func_b(b)[5]);
                    putFloatLn(func_a(a)[5]*func_b(b)[5]);
                    putFloatLn(func_b(b)[5]/func_a(a)[5]);
                    putFloatLn(func_a(a)[5]+func_b(b)[5]*func_a(a)[5]+func_b(b)[5]/func_a(a)[5]-func_a(a)[5]/func_b(b)[5]);

                    putBoolLn(func_a(a)[5]+func_b(b)[5] >= func_b(b)[5]-func_a(a)[5]+func_a(a)[5]+func_a(a)[5]);
                    putBoolLn(func_a(a)[5]+func_b(b)[5] >= func_b(b)[5]-func_a(a)[5]);
                    putBoolLn(func_a(a)[5] >= func_b(b)[5]+func_a(a)[5]);
                    putBoolLn(func_a(a)[5]+func_b(b)[5] > func_b(b)[5]-func_a(a)[5]);
                    putBoolLn(func_a(a)[5]+func_b(b)[5] > func_b(b)[5]-func_a(a)[5]+func_a(a)[5]+func_a(a)[5]);
                    putBoolLn(func_a(a)[5] > func_a(a)[5]+func_b(b)[5]);

                    putBoolLn(func_a(a)[5]+func_b(b)[5] <= func_b(b)[5]-func_a(a)[5]+func_a(a)[5]+func_a(a)[5]);
                    putBoolLn(func_a(a)[5]+func_b(b)[5] <= func_b(b)[5]-func_a(a)[5]);
                    putBoolLn(func_a(a)[5] <= func_b(b)[5]+func_a(a)[5]);
                    putBoolLn(func_a(a)[5]+func_b(b)[5] < func_b(b)[5]-func_a(a)[5]);
                    putBoolLn(func_a(a)[5]+func_b(b)[5] < func_b(b)[5]-func_a(a)[5]+func_a(a)[5]+func_a(a)[5]);
                    putBoolLn(func_a(a)[5] < func_a(a)[5]+func_b(b)[5]);

                    putFloatLn(-(func_a(a)[5]+func_b(b)[5]));
                }
                void main(){
                    a[5] = 2;
                    b[5] = 5.1;
                    func(a,b);
                }
                """
        expect = "7.1\n-3.1\n10.2\n2.55\n14.357843\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\nfalse\ntrue\nfalse\nfalse\ntrue\n-7.1\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    #if statement
    def test_if_statement(self):
        input = """
                void main(){
                    if(true){
                        putStringLn("true");
                    }
                    if(true)    putStringLn("true1");
                    if(false){
                        putStringLn("false");
                    }
                    if(false)   putStringLn("false");
                }
                """
        expect = "true\ntrue1\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_if_else_statement(self):
        input = """
                void main(){
                    if(false){
                        putStringLn("true");
                    } else{
                        putStringLn("false");
                    }

                    if(false)    putStringLn("true");
                    else putStringLn("false");
                }
                """
        expect = "false\nfalse\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    #do while statement
    def test_do_while_statement(self):
        input = """
                void main(){
                    int i;
                    i = 0;
                    do{
                        i = i + 1;
                        putIntLn(i);
                    }while i < 5;

                    i = 0;
                    do
                        putIntLn(i = i + 1);
                    while i < 5;

                    i = 0;
                    do
                        putIntLn(i);
                    while (i = i+1) < 5;
                }
                """
        expect = "1\n2\n3\n4\n5\n1\n2\n3\n4\n5\n0\n1\n2\n3\n4\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    #for statement
    def test_for_statement(self):
        input = """
                void main(){
                    int i;
                    for (i = 1; i < 3; i = i + 1)
                        putIntLn(i);
                    for (i = 1; i < 3; i = i + 1){
                        putIntLn(i);
                    }
                }
                """
        expect = "1\n2\n1\n2\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    #break statement
    def test_break_statement(self):
        input = """
                void main(){
                    int i;
                    for (i = 1; i < 5; i = i + 1){
                        if (i > 3){
                            break;
                        }
                        putIntLn(i);
                    }

                    i = 1;
                    do{
                        i = i + 1;
                        if (i > 3){
                            break;
                        }
                        putIntLn(i);
                    }while (i <5);
                }
                """
        expect = "1\n2\n3\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    #continue statement
    def test_continue_statement(self):
        input = """
                void main(){
                    int i;
                    for (i = 1; i < 5; i = i + 1){
                        if (i%2 == 1){
                            continue;
                        }
                        putIntLn(i);
                    }

                    i = 1;
                    do{
                        i = i + 1;
                        if (i%2 == 1){
                            continue;
                        }
                        putIntLn(i);
                    }while (i <5);
                }
                """
        expect = "2\n4\n2\n4\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_(self):
        input = """
                void main(){
                    int a,b,c;
                    putIntLn(a= (b=100) + (c=5));
                    putIntLn(a);
                    putIntLn(b);
                    putIntLn(c);
                }
                """
        expect = "105\n105\n100\n5\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_2(self):
        input = """
                void main() {
                    int a, b;
                    putInt(1 + (a=2));
                }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    #Recursive func
    def test_recursive_func(self):
        input = """
                int fibo(int a)
                {
                    if (a <= 1) return a;
                    else return fibo(a-1) + fibo(a-2);
                }
                void main() {
                    putIntLn(fibo(0));
                    putIntLn(fibo(2));
                    putIntLn(fibo(8));
                    putIntLn(fibo(12));
                }
        """
        expect = "0\n1\n21\n144\n"
        self.assertTrue(TestCodeGen.test(input,expect,501))