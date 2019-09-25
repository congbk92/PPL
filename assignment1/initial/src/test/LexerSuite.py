import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    #1.Test identifiers
    def test_id_lower(self):
        self.assertTrue(TestLexer.checkLexeme("abcghjndghjdt","abcghjndghjdt,<EOF>",101))
    def test_id_upper(self):
        self.assertTrue(TestLexer.checkLexeme("ZBSDFGHASASDCV","ZBSDFGHASASDCV,<EOF>",102))
    def test_id_lower_upper(self):
        self.assertTrue(TestLexer.checkLexeme("aCBbdHLhouhBNIUc","aCBbdHLhouhBNIUc,<EOF>",103))
    def test_id_all_type(self):
        self.assertTrue(TestLexer.checkLexeme("_aCB5623452_b41_dHLhou4735_____hBNIUc","_aCB5623452_b41_dHLhou4735_____hBNIUc,<EOF>",104))
    def test_id_with_ws(self):
        self.assertTrue(TestLexer.checkLexeme("_aCB5623452_\nb41_dH\rLhou4735___\t__hBNIUc","_aCB5623452_,b41_dH,Lhou4735___,__hBNIUc,<EOF>",104))

    #2.Test keywords
    def test_keyword_ws(self):
        self.assertTrue(TestLexer.checkLexeme("break\tcontinue\relse\nfor float\tif\nint\rreturn void\tdo\nwhile\rtrue false",
            "break,continue,else,for,float,if,int,return,void,do,while,true,false,<EOF>",120))
    def test_keyword_separator(self):
        self.assertTrue(TestLexer.checkLexeme("break[continue]else}for{float)if(int,return;void;do;while;true;false",
            "break,[,continue,],else,},for,{,float,),if,(,int,,,return,;,void,;,do,;,while,;,true,;,false,<EOF>",121))

    def test_keyword_failcase(self):
        self.assertTrue(TestLexer.checkLexeme("breakcontinueelseforfloatifintreturnvoiddowhiletruefalse",
            "breakcontinueelseforfloatifintreturnvoiddowhiletruefalse,<EOF>",122))

    #3.Test operators
    def test_operator_ws(self):
        self.assertTrue(TestLexer.checkLexeme("int void\tboolean\rfloat\nstring","int,void,boolean,float,string,<EOF>",130))
    def test_operator_separator(self):
        self.assertTrue(TestLexer.checkLexeme("int[void]boolean{float}str ing();,","int,[,void,],boolean,{,float,},str,ing,(,),;,,,<EOF>",131))

    #4.Test separators
    def test_separator(self):
        self.assertTrue(TestLexer.checkLexeme("[]{}();,","[,],{,},(,),;,,,<EOF>",141))

    #5.Test literals
        #1.interger
    def test_integer_id(self):
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",150))
    def test_integer_mid_id(self):
        self.assertTrue(TestLexer.checkLexeme("_123a123","_123a123,<EOF>",151))
    def test_integer_mid_id_1(self):
        self.assertTrue(TestLexer.checkLexeme("_a123ajghjdgh412342","_a123ajghjdgh412342,<EOF>",152))
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
        self.assertTrue(TestLexer.checkLexeme("\"This is nomal string\"","\"This is nomal string\",<EOF>",170))   
    #def test_string_normal_endline(self):
        #self.assertTrue(TestLexer.checkLexeme("\"This is a nomal string \\n with endline\"","This is a nomal string \n with endline",171))
    
    #6.Comment and ws
    def test_comment_single_line(self):
        self.assertTrue(TestLexer.checkLexeme("//This is a line comments","<EOF>",180))
    def test_comment_single_line_multi(self):
        self.assertTrue(TestLexer.checkLexeme("////This is a line/// comments///","<EOF>",181))
    def test_comment_single_line_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("//break continue else for float if int return void do while true false","<EOF>",182))
    def test_comment_single_line_operator_ws(self):
        self.assertTrue(TestLexer.checkLexeme("//+ - * / ! % | && != == < > <= >= = \t \r","<EOF>",183))
    def test_comment_single_line_id(self):
        self.assertTrue(TestLexer.checkLexeme("//This is a line comments\n123abc123","123,abc123,<EOF>",184))        
    def test_comment_multi_line_1(self):
        self.assertTrue(TestLexer.checkLexeme("/*This is a comment, 42341v%@%^&#$^&@$v dfvaf$@#%@!#$GSADF5245*****/","<EOF>",185))
    def test_comment_multi_line_2(self):
        self.assertTrue(TestLexer.checkLexeme("/*This is a comment, \n \n \n \n \r\t 42341v%@%^&#$^&@$v dfvaf$@#%@!#$GSADF5245*****/","<EOF>",186))
    def test_comment_multi_line_3(self):
        self.assertTrue(TestLexer.checkLexeme("/*This /**/","<EOF>",187))
    def test_comment_multi_line_4(self):
        self.assertTrue(TestLexer.checkLexeme("/*This \n/**///%$@#%$@#%4","<EOF>",188)) 
    def test_comment_multi_line_5(self):
        self.assertTrue(TestLexer.checkLexeme("/*This /**/*/","*,/,<EOF>",189))
    def test_comment_multi_line_6(self):
        self.assertTrue(TestLexer.checkLexeme("/*This /**/*//Comment","*,<EOF>",190)) 
    #7.Test wrong cases
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("aA?sVN","aA,Error Token ?",191))
    #8.Other