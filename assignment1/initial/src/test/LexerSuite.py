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
        self.assertTrue(TestLexer.checkLexeme("boolean break\tcontinue\relse\nfor float\tif\nint\rreturn void\tdo\nwhile\rtrue false string",
            "boolean,break,continue,else,for,float,if,int,return,void,do,while,true,false,string,<EOF>",120))
    def test_keyword_separator(self):
        self.assertTrue(TestLexer.checkLexeme("boolean;break[continue]else}for{float)if(int,return;void;do;while;true;false;string",
            "boolean,;,break,[,continue,],else,},for,{,float,),if,(,int,,,return,;,void,;,do,;,while,;,true,;,false,;,string,<EOF>",121))

    def test_keyword_failcase(self):
        self.assertTrue(TestLexer.checkLexeme("booleanbreakcontinueelseforfloatifintreturnvoiddowhiletruefalsestring",
            "booleanbreakcontinueelseforfloatifintreturnvoiddowhiletruefalsestring,<EOF>",122))

    #3.Test operators

    #4.Test separators
    #5.Test literals
        #1.interger
    def test_integer_id(self):
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",130))
    def test_integer_mid_id(self):
        self.assertTrue(TestLexer.checkLexeme("_123a123","_123a123,<EOF>",131))
    def test_integer_mid_id_1(self):
        self.assertTrue(TestLexer.checkLexeme("_a123ajghjdgh412342","_a123ajghjdgh412342,<EOF>",132))
        #2.float
        #3.boolean
        #4.string
    #6.Comment and ws
    def test_comment_single_line(self):
        self.assertTrue(TestLexer.checkLexeme("//This is a line comments","<EOF>",180))
    def test_comment_multi_line(self):
        self.assertTrue(TestLexer.checkLexeme("/*This is a comment, \n \n \n \n \r\t 42341v%@%^&#$^&@$v dfvaf$@#%@!#$GSADF5245*****/","<EOF>",185))
    #7.Test wrong cases
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("aA?sVN","aA,Error Token ?",190))