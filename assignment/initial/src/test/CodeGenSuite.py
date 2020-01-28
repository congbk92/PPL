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
                    putFloat(10*10 + 100.4/2 - 15*2.3 + 2.2/1.2);
                }"""
        expect = "117.53333"
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