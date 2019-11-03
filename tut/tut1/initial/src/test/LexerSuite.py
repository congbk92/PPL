import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
 
        #2.float
    def test_float_normal_dot_only(self):
        self.assertTrue(TestLexer.checkLexeme("1.2 1. .11.1.2 ","1.2,1.,.11,.1,.2,<EOF>",160))
    def test_float_abnormal_dot_only(self):
        self.assertTrue(TestLexer.checkLexeme("01234 . ","01234,Error Token .",161))
    def test_float_normal_Ee_dot(self):
        self.assertTrue(TestLexer.checkLexeme("1.2E5 1.2e5 .1E2 .1e5 1.2E51.2e5","1.2E5,1.2e5,.1E2,.1e5,1.2E51,.2e5,<EOF>",162))   
    def test_float_abnormal_Ee_dot(self):
        self.assertTrue(TestLexer.checkLexeme("1.E5 1.2e .1E .2E51.e","1.E5,1.2,e,.1,E,.2E51,Error Token .",163))   
    def test_float_normal_Ee_dot_sub(self):
        self.assertTrue(TestLexer.checkLexeme("1.2E-5 1.2e-5 .1E-2 .1e-5 1.2E-51.2e-5","1.2E-5,1.2e-5,.1E-2,.1e-5,1.2E-51,.2e-5,<EOF>",164))   
    def test_float_abnormal_Ee_dot_sub(self):
        self.assertTrue(TestLexer.checkLexeme("1.E-5 1.2e- .1E- 1..3E-2 .2E-51.e-","1.E-5,1.2,e,-,.1,E,-,1.,.3E-2,.2E-51,Error Token .",165))   
    def test_float_normal_Ee_sub(self):
        self.assertTrue(TestLexer.checkLexeme("1E-5 1e-5 1E-51e-5","1E-5,1e-5,1E-51,e,-,5,<EOF>",164))   
    def test_float_abnormal_Ee_sub(self):
        self.assertTrue(TestLexer.checkLexeme("eeEE- e-5 5E- e-55E-","eeEE,-,e,-,5,5,E,-,e,-,55,E,-,<EOF>",165))  
    def test_float_normal_Ee_sub(self):
        self.assertTrue(TestLexer.checkLexeme("1E-5 1e-5 1E-51e-5","1E-5,1e-5,1E-51,e,-,5,<EOF>",164))   
    def test_float_abnormal_Ee_sub(self):
        self.assertTrue(TestLexer.checkLexeme("eeEE- e-5 5E- e-55E-","eeEE,-,e,-,5,5,E,-,e,-,55,E,-,<EOF>",165))   
    def test_float_abnormal_sub_dot(self):
        self.assertTrue(TestLexer.checkLexeme("1ee-.","1,ee,-,Error Token .",166))   
    def test_float_abnormal_double_eE(self):
        self.assertTrue(TestLexer.checkLexeme("1ee1 1EE1 5Ee1 1eE1","1,ee1,1,EE1,5,Ee1,1,eE1,<EOF>",167))   
    def test_float_abnormal_double_sub(self):
        self.assertTrue(TestLexer.checkLexeme("1e--1 1E--1","1,e,-,-,1,1,E,-,-,1,<EOF>",168))
    def test_float_abnormal_multi_dot(self):
        self.assertTrue(TestLexer.checkLexeme("1..3e1 1...3e1","1.,.3e1,1.,Error Token .",169))         
        #3.boolean
        #4.string
    
    def test_string_normal(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is a nomal string\"","\"This is a nomal string\"",170))   
    def test_string_normal_endline(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is a nomal string \\n with endline\"","\"This is a nomal string \n with endline\"",171))
    