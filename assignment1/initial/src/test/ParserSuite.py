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
#1.Declare
    #1. Declare variable        
    def test_declare_int_variable(self):
        input = """int main () {
            int abcd;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21101))
    def test_declare_bool_variable(self):
        input = """int main () {
            boolean abcd;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21102))
    def test_declare_float_variable(self):
        input = """int main () {
            float abcd;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21103))
    def test_declare_string_variable(self):
        input = """int main () {
            string abcd;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21104))

    def test_declare_multi_variable(self):        
        input = """int main () {
            int abcd;
            float abcd1;
            boolean abcd341;
            string fads342r5;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21105))

    def test_declare_multi_list_variable(self):        
        input = """int main () {
            int abcd,_21312,sa1;
            float abcd,_21312,sa1;
            boolean abcd,_21312,sa1;
            string abcd,_21312,sa1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21106))
    
    def test_abnormal_declare_variable_and_init(self):        
        input = """int main () {
                int a = 1;
        }"""
        expect = "Error on line 2 col 22: ="
        self.assertTrue(TestParser.checkParser(input,expect,21107))

    ''' Need Fix
    def test_abnormal_declare_variable_miss_semi(self):        
        input = """int main () {
                bool a
        }"""
        expect = "Error on line 2 col 21: a"
        self.assertTrue(TestParser.checkParser(input,expect,21108))
    '''
    
    #2. Declare array
    def test_declare_int_arr(self):
        input = """int main () {
            int abcd[1];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21201))
    def test_declare_bool_arr(self):
        input = """int main () {
            boolean abcd[32];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21202))
    def test_declare_float_arr(self):
        input = """int main () {
            float abcd[54];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21203))
    def test_declare_string_arr(self):
        input = """int main () {
            string abcd[76];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21204))

    def test_declare_multi_arr(self):        
        input = """int main () {
            int abcd[4];
            float abcd1[54];
            boolean abcd341[5];
            string fads342r5[8];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21205))

    def test_declare_multi_list_arr(self):        
        input = """int main () {
            int abcd[54],_21312[54],sa1[54];
            float abcd[2],_21312[8],sa1[8];
            boolean abcd[5],_21312[8],sa1[7];
            string abcd[6],_21312[9],sa1[0];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,21206))
    
    def test_abnormal_declare_arr_and_init(self):        
        input = """int main () {
                int a[3] = 1;
        }"""
        expect = "Error on line 2 col 25: ="
        self.assertTrue(TestParser.checkParser(input,expect,21207))

    def test_abnormal_declare_arr_miss_semi(self):        
        input = """int main () {
                int a[3]
        }"""
        expect = "Error on line 3 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,21208))

    def test_abnormal_declare_list_arr_miss_coma(self):        
        input = """int main () {
                int a[3]b[6];
        }"""
        expect = "Error on line 2 col 24: b"
        self.assertTrue(TestParser.checkParser(input,expect,21209))

    def test_abnormal_declare_arr_undefine(self):        
        input = """int main () {
                int abf[];
        }"""
        expect = "Error on line 2 col 24: ]"
        self.assertTrue(TestParser.checkParser(input,expect,21210))




    def test_scope(self):        
        input = """int main () {
                {
                    int a;
                    abcd();
                }
                putIntLn(4);
                int a1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,0))

    def test_multi_scope(self):        
        input = """int main () {
                {
                    int a;
                    abcd();
                    {
                        putIntLn(4);
                        int a1;
                    }
                }
                putIntLn(4);
                int a1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,0))

    def test_draff(self):        
        input = """int main () {
                {
                    int a;
                    abcd(abcd[a+b*c+d*e]);
                    {
                        putIntLn(4);
                        int a1;
                    }
                    if (abcd[a+c+b+d] + 1.2 > abce + 143 + fdsfs ) a = a+a;
                }
                putIntLn(4);
                int a1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,111111))

    '''
    def test_declare_list_variable(self):
        """Miss ) int main( {}"""
        input = """int abcd,_56748, ab423cd;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    '''