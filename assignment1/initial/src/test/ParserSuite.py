import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_simple_program_with_comment(self):
        """Simple program: int main() {} """
        input = """int main() 
        {
            //comment in here
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_simple_program_with_multiline_comment(self):
        """Simple program: int main() {} """
        input = """int main() 
        {
            /*
            comment in here
            */
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,205))
        
    def test_declare_variable(self):
        """Miss ) int main( {}"""
        input = """int main () {
            putIntLn(4);
            int abcd;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_declare_multi_variable(self):
        """Miss ) int main( {}"""
        input = """int main () {
            putIntLn(4);
            int abcd;
            int abcd1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_declare_list_variable(self):
        """Miss ) int main( {}"""
        input = """int main () {
            putIntLn(4);
            int abcd,_21312,sa1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_declare_multi_list_variable(self):
        """Miss ) int main( {}"""
        input = """int main () {
            putIntLn(4);
            int abcd,_21312,sa1;
            int abcdfaf,_21fdsaf312,sdfaa1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    
    '''
    def test_declare_list_variable(self):
        """Miss ) int main( {}"""
        input = """int abcd,_56748, ab423cd;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    '''