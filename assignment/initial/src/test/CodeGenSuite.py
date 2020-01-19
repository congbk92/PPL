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
        input = """void main() {
                    putInt(100);
                }"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_float_ast(self):
        input = """void main() {
                    putFloat(100.001);
                }"""
        expect = "100.001"
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
        self.assertTrue(TestCodeGen.test(input,expect,501))
    '''
    def test_id(self):
        input = """void main() {
                    int a;
                    a = 100;
                    putInt(a);
                }"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    '''