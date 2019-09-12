import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("aA?sVN","aA,Error Token ?",103))
    def test_integer(self):
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",104))
    def test_integer_mid_id(self):
        self.assertTrue(TestLexer.checkLexeme("_123a123","_123a123,<EOF>",105))
    def test_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("boolean break continue else for float if int return void do while true false string",
            "boolean,break,continue,else,for,float,if,int,return,void,do,while,true,false,string,<EOF>",106))