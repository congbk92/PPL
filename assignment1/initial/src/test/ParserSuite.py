import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program_with_comment(self):
        """Simple program: int main() {} """
        input = """int main() 
        {
            //comment in here
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
    def test_simple_program_with_multiline_comment(self):
        """Simple program: int main() {} """
        input = """int main() 
        {
            /*
            comment in here
            */
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))
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

#Actual testcase
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
        
    def test_decl_global_variable(self):
        input = """int _abcd;
                    boolean ab13;
                    float abcd;
                    string abcde;
                    int _abcd[312];
                    boolean ab13[523];
                    float abcd[5];
                    string abcde[542];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
        
    def test_decl_global_variable(self):
        input = """int _abcd,dfda,gdsfg[43];
                    boolean ab13,fdas3,fdas,rtg[534];
                    float abcd,ghrt5,gfg[76];
                    string abcde,kryu,gghrtft[87];
                    int _abcd[312],grdfg,gfds,gsdfg,rtwe,trw,wtre;
                    boolean ab13[523],rewtwe,rtewt[543],wete5twe,twertw;
                    float abcd[5],twertwe,gdfsg ,twer[534], wt[534], tw;
                    string abcde[542],trew[65],trew[54],trewt,wre;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
        
    def test_decl_func_empt_param_body(self):
        input = """int _abcd() {}
                    boolean ab13() {}
                    float abcd() {}
                    string abcde(){}
                    void kjk() {}
                    int[] _abcd(){}
                    boolean[] ab13(){}
                    float[] abcd(){}
                    string[] abcde(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
        
    def test_decl_func_empt_body(self):
        input = """int _abcd(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]) {}
                boolean ab13(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]) {}
                float abcd(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]) {}
                string abcde(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                void kjk(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]) {}
                int[] _abcd(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                boolean[] ab13(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                float[] abcd(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}
                string[] abcde(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
        
    def test_decl_func_variable(self):
        input = """
                    int _abcd,dfda,gdsfg[43];
                    boolean ab13,fdas3,fdas,rtg[534];
                    float abcd,ghrt5,gfg[76];
                    string abcde,kryu,gghrtft[87];
                    int _abcd[312],grdfg,gfds,gsdfg,rtwe,trw,wtre;
                    boolean ab13[523],rewtwe,rtewt[543],wete5twe,twertw;
                    float abcd[5],twertwe,gdfsg ,twer[534], wt[534], tw;
                    string abcde[542],trew[65],trew[54],trewt,wre;
                    int _abcd(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]) 
                    {
                        int _abcd,dfda,gdsfg[43];
                        boolean ab13,fdas3,fdas,rtg[534];
                        float abcd,ghrt5,gfg[76];
                        string abcde,kryu,gghrtft[87];
                        int _abcd[312],grdfg,gfds,gsdfg,rtwe,trw,wtre;
                        boolean ab13[523],rewtwe,rtewt[543],wete5twe,twertw;
                        float abcd[5],twertwe,gdfsg ,twer[534], wt[534], tw;
                        string abcde[542],trew[65],trew[54],trewt,wre;
                    }
                    boolean ab13(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]) 
                    {
                        int _abcd,dfda,gdsfg[43];
                        boolean ab13,fdas3,fdas,rtg[534];
                        float abcd,ghrt5,gfg[76];
                        string abcde,kryu,gghrtft[87];
                        int _abcd[312],grdfg,gfds,gsdfg,rtwe,trw,wtre;
                        boolean ab13[523],rewtwe,rtewt[543],wete5twe,twertw;
                        float abcd[5],twertwe,gdfsg ,twer[534], wt[534], tw;
                        string abcde[542],trew[65],trew[54],trewt,wre;
                    }
                    float abcd(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]) 
                    {
                        int _abcd,dfda,gdsfg[43];
                        boolean ab13,fdas3,fdas,rtg[534];
                        float abcd,ghrt5,gfg[76];
                        string abcde,kryu,gghrtft[87];
                        int _abcd[312],grdfg,gfds,gsdfg,rtwe,trw,wtre;
                        boolean ab13[523],rewtwe,rtewt[543],wete5twe,twertw;
                        float abcd[5],twertwe,gdfsg ,twer[534], wt[534], tw;
                        string abcde[542],trew[65],trew[54],trewt,wre;
                    }
                    string abcde(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                    {
                        int _abcd,dfda,gdsfg[43];
                        boolean ab13,fdas3,fdas,rtg[534];
                        float abcd,ghrt5,gfg[76];
                        string abcde,kryu,gghrtft[87];
                        int _abcd[312],grdfg,gfds,gsdfg,rtwe,trw,wtre;
                        boolean ab13[523],rewtwe,rtewt[543],wete5twe,twertw;
                        float abcd[5],twertwe,gdfsg ,twer[534], wt[534], tw;
                        string abcde[542],trew[65],trew[54],trewt,wre;
                    }
                    void kjk(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[]) 
                    {
                        int _abcd,dfda,gdsfg[43];
                        boolean ab13,fdas3,fdas,rtg[534];
                        float abcd,ghrt5,gfg[76];
                        string abcde,kryu,gghrtft[87];
                        int _abcd[312],grdfg,gfds,gsdfg,rtwe,trw,wtre;
                        boolean ab13[523],rewtwe,rtewt[543],wete5twe,twertw;
                        float abcd[5],twertwe,gdfsg ,twer[534], wt[534], tw;
                        string abcde[542],trew[65],trew[54],trewt,wre;
                    }
                    int[] _abcd(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                    {
                        int _abcd,dfda,gdsfg[43];
                        boolean ab13,fdas3,fdas,rtg[534];
                        float abcd,ghrt5,gfg[76];
                        string abcde,kryu,gghrtft[87];
                        int _abcd[312],grdfg,gfds,gsdfg,rtwe,trw,wtre;
                        boolean ab13[523],rewtwe,rtewt[543],wete5twe,twertw;
                        float abcd[5],twertwe,gdfsg ,twer[534], wt[534], tw;
                        string abcde[542],trew[65],trew[54],trewt,wre;
                    }
                    boolean[] ab13(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                    {
                        int _abcd,dfda,gdsfg[43];
                        boolean ab13,fdas3,fdas,rtg[534];
                        float abcd,ghrt5,gfg[76];
                        string abcde,kryu,gghrtft[87];
                        int _abcd[312],grdfg,gfds,gsdfg,rtwe,trw,wtre;
                        boolean ab13[523],rewtwe,rtewt[543],wete5twe,twertw;
                        float abcd[5],twertwe,gdfsg ,twer[534], wt[534], tw;
                        string abcde[542],trew[65],trew[54],trewt,wre;
                    }
                    float[] abcd(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                    {
                        int _abcd,dfda,gdsfg[43];
                        boolean ab13,fdas3,fdas,rtg[534];
                        float abcd,ghrt5,gfg[76];
                        string abcde,kryu,gghrtft[87];
                        int _abcd[312],grdfg,gfds,gsdfg,rtwe,trw,wtre;
                        boolean ab13[523],rewtwe,rtewt[543],wete5twe,twertw;
                        float abcd[5],twertwe,gdfsg ,twer[534], wt[534], tw;
                        string abcde[542],trew[65],trew[54],trewt,wre;
                    }
                    string[] abcde(int a, boolean b, float c, string d, int a[], boolean b[], float c[], string d[])
                    {
                        int _abcd,dfda,gdsfg[43];
                        boolean ab13,fdas3,fdas,rtg[534];
                        float abcd,ghrt5,gfg[76];
                        string abcde,kryu,gghrtft[87];
                        int _abcd[312],grdfg,gfds,gsdfg,rtwe,trw,wtre;
                        boolean ab13[523],rewtwe,rtewt[543],wete5twe,twertw;
                        float abcd[5],twertwe,gdfsg ,twer[534], wt[534], tw;
                        string abcde[542],trew[65],trew[54],trewt,wre;
                    }
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
        
    def test_wrong_decl_void_global_variable(self):
        input = """void a;"""
        expect = "Error on line 1 col 6: ;"
        self.assertTrue(TestParser.checkParser(input,expect,209))
        
    def test_wrong_decl_void_local_variable(self):
        input = """void functest()
                {
                    void a;
                }"""
        expect = "Error on line 3 col 20: void"
        self.assertTrue(TestParser.checkParser(input,expect,210))
        
    def test_wrong_decl_init_global_int_variable(self):
        input = """int abdffre = 1;"""
        expect = "Error on line 1 col 12: ="
        self.assertTrue(TestParser.checkParser(input,expect,211))
        
    def test_wrong_decl_init_global_float_variable(self):
        input = """float abdffre = 142134.e3421;"""
        expect = "Error on line 1 col 14: ="
        self.assertTrue(TestParser.checkParser(input,expect,212))
        
    def test_wrong_decl_init_global_boolean_variable(self):
        input = """boolean abdffre = true;"""
        expect = "Error on line 1 col 16: ="
        self.assertTrue(TestParser.checkParser(input,expect,213))
        
    def test_wrong_decl_init_global_string_variable(self):
        input = """string abdffre = true;"""
        expect = "Error on line 1 col 15: ="
        self.assertTrue(TestParser.checkParser(input,expect,214))
        
    def test_wrong_decl_init_global_arr_variable(self):
        input = """int abdffre[123] = {1,2,3};"""
        expect = "Error on line 1 col 17: ="
        self.assertTrue(TestParser.checkParser(input,expect,215))
        
    def test_wrong_decl_init_local_int_variable(self):
        input = """int abdffre;
                    int abncd()
                    {
                        int abdffre = 1;
                    }"""
        expect = "Error on line 4 col 36: ="
        self.assertTrue(TestParser.checkParser(input,expect,216))
        
    def test_wrong_decl_init_local_float_variable(self):
        input = """int abdffre;
                    void main()
                    {
                        float abdffre = 142134.e3421;
                    }"""
        expect = "Error on line 4 col 38: ="
        self.assertTrue(TestParser.checkParser(input,expect,217))
        
    def test_wrong_decl_init_local_boolean_variable(self):
        input = """boolean abdffre;
                    float avda()
                    {
                        boolean abdffre = true;
                    }"""
        expect = "Error on line 4 col 40: ="
        self.assertTrue(TestParser.checkParser(input,expect,218))
        
    def test_wrong_decl_init_local_string_variable(self):
        input = """string abdffre;
                    boolean trqewte()
                    {
                        string abdffre = true;
                    }"""
        expect = "Error on line 4 col 39: ="
        self.assertTrue(TestParser.checkParser(input,expect,219))
        
    def test_wrong_decl_init_local_arr_variable(self):
        input = """int abdffre[123];
                    string badgdfa()
                    {
                        boolean abdffre[3] = {true,false,true};
                    }
                    """
        expect = "Error on line 4 col 43: ="
        self.assertTrue(TestParser.checkParser(input,expect,220))
    
    def test_wrong_decl_arr_without_size(self):
        input = """int abdffre[123];
                    string badgdfa()
                    {
                        boolean abdffre[];
                    }
                    """
        expect = "Error on line 4 col 40: ]"
        self.assertTrue(TestParser.checkParser(input,expect,221))
        
    def test_wrong_decl_arr_invalid_size_1(self):
        input = """int abdffre[123 + 32];
                    """
        expect = "Error on line 1 col 16: +"
        self.assertTrue(TestParser.checkParser(input,expect,222))       
        
    def test_wrong_decl_arr_invalid_size_2(self):
        input = """float abdffre[123dasdas];"""
        expect = "Error on line 1 col 17: dasdas"
        self.assertTrue(TestParser.checkParser(input,expect,223))   
    
    def test_wrong_decl_arr_invalid_size_3(self):
        input = """boolean abdffre[123.54];"""
        expect = "Error on line 1 col 16: 123.54"
        self.assertTrue(TestParser.checkParser(input,expect,224))       
    
    def test_wrong_decl_arr_invalid_size_4(self):
        input = """string abdffre[true];"""
        expect = "Error on line 1 col 15: true"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    
    def test_wrong_decl_func_missing_type(self):
        input = """func(){}"""
        expect = "Error on line 1 col 0: func"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    
    def test_wrong_decl_func_invalid_type_1(self):
        input = """abcde func(){}"""
        expect = "Error on line 1 col 0: abcde"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    
    def test_wrong_decl_func_invalid_type_2(self):
        input = """123string func(){}"""
        expect = "Error on line 1 col 0: 123"
        self.assertTrue(TestParser.checkParser(input,expect,228))
        
    def test_wrong_decl_func_missing_func_name(self):
        input = """boolean (){}"""
        expect = "Error on line 1 col 8: ("
        self.assertTrue(TestParser.checkParser(input,expect,229))   

    def test_wrong_decl_func_invalid_func_name_1(self):
        input = """boolean 123bssfd(){}"""
        expect = "Error on line 1 col 8: 123"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    
    def test_wrong_decl_func_invalid_func_name_2(self):
        input = """boolean string(){}"""
        expect = "Error on line 1 col 8: string"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    
    def test_wrong_decl_func_invalid_param_1(self):
        input = """boolean func(void a){}"""
        expect = "Error on line 1 col 13: void"
        self.assertTrue(TestParser.checkParser(input,expect,232))
        
    def test_wrong_decl_func_invalid_param_2(self):
        input = """string testFunc(abcde){}"""
        expect = "Error on line 1 col 16: abcde"
        self.assertTrue(TestParser.checkParser(input,expect,233))   
    
    def test_wrong_decl_func_invalid_param_3(self):
        input = """boolean func(string){}"""
        expect = "Error on line 1 col 19: )"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    
    def test_wrong_decl_func_invalid_param_4(self):
        input = """string adsa(int 12abcde){}"""
        expect = "Error on line 1 col 16: 12"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    
    def test_wrong_decl_func_invalid_param_5(self):
        input = """int fdasf(int abcde,string a[123]){}"""
        expect = "Error on line 1 col 29: 123"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    
    def test_wrong_decl_func_invalid_param_6(self):
        input = """float func(int abcde,string a[],){}"""
        expect = "Error on line 1 col 32: )"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    
    def test_wrong_decl_func_missing_param(self):
        input = """float func{}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    
    def test_wrong_decl_func_missing_block_stmt(self):
        input = """float func(int abcde,string a[])"""
        expect = "Error on line 1 col 32: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    
    def test_wrong_decl_func_invalid_block_stmt_1(self):
        input = """float func(int abcde,string a[]){};"""
        expect = "Error on line 1 col 34: ;"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    
    def test_wrong_decl_func_invalid_block_stmt_2(self):
        input = """float func(int abcde,string a[]){"""
        expect = "Error on line 1 col 33: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    
    def test_wrong_decl_func_invalid_block_stmt_3(self):
        input = """float func(int abcde,string a[])}"""
        expect = "Error on line 1 col 32: }"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    
    def test_wrong_decl_func_nested(self):
        input = """void func1(int abcde,string a[])
                {
                    string func2(int abcde){}
                }
                """
        expect = "Error on line 3 col 32: ("
        self.assertTrue(TestParser.checkParser(input,expect,243))
        
    def test_wrong_program_empty(self):
        input = """ """
        expect = "Error on line 1 col 1: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,244))
        
    def test_wrong_program_statement_outside_func(self):
        input = """int a,b,c;
                    a = b + c;"""
        expect = "Error on line 2 col 20: a"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    # Test type and expression
    def test_boolean_type(self):
        input = """void testFunc()
        {
            a = true == false;
            b = true != false;
            c = !true;
            d = true && false;
            e = true || false;
            true == false;
            true != false;
            !true;
            true && false;
            true || false;
            1 == 2 && 2 != 54;
            1 > 2 || 2.54 < 54;
            1 >= 2.e43 && 2.33e-2 <= 54e54;
            func(1 >= 2.e43 && 2.33e-2 <= 54e54);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
        
    def test_wrong_boolean_type_1(self):
        input = """void testFunc()
        {
            a = true[123];
        }"""
        expect = "Error on line 3 col 20: ["
        self.assertTrue(TestParser.checkParser(input,expect,247))
        
    def test_wrong_boolean_type_2(self):
        input = """void testFunc()
        {
            b = -true;
        }"""
        expect = "Error on line 3 col 17: true"
        self.assertTrue(TestParser.checkParser(input,expect,248))
        
    def test_wrong_boolean_type_3(self):
        input = """void testFunc()
        {
            b = true/false;
        }"""
        expect = "Error on line 3 col 20: /"
        self.assertTrue(TestParser.checkParser(input,expect,249))
        
    def test_wrong_boolean_type_4(self):
        input = """void testFunc()
        {
            b = true*false;
        }"""
        expect = "Error on line 3 col 20: *"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    
    def test_wrong_boolean_type_5(self):
        input = """void testFunc()
        {
            b = true%false;
        }"""
        expect = "Error on line 3 col 20: %"
        self.assertTrue(TestParser.checkParser(input,expect,251))
        
    def test_wrong_boolean_type_6(self):
        input = """void testFunc()
        {
            b = true+false;
        }"""
        expect = "Error on line 3 col 20: +"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_wrong_boolean_type_7(self):
        input = """void testFunc()
        {
            b = true - false;
        }"""
        expect = "Error on line 3 col 21: -"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_wrong_boolean_type_8(self):
        input = """void testFunc()
        {
            b = true > false;
        }"""
        expect = "Error on line 3 col 21: >"
        self.assertTrue(TestParser.checkParser(input,expect,254))
        
    def test_wrong_boolean_type_9(self):
        input = """void testFunc()
        {
            b = true >= false;
        }"""
        expect = "Error on line 3 col 21: >="
        self.assertTrue(TestParser.checkParser(input,expect,255))
        
    def test_wrong_boolean_type_10(self):
        input = """void testFunc()
        {
            b = true < false;
        }"""
        expect = "Error on line 3 col 21: <"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    
    def test_wrong_boolean_type_11(self):
        input = """void testFunc()
        {
            b = true <= false;
        }"""
        expect = "Error on line 3 col 21: <="
        self.assertTrue(TestParser.checkParser(input,expect,257))
        
    def test_int_type(self):
        input = """void testFunc()
        {
            f = -423;
            12 + 21;
            43 - 231;
            32 * 4324;
            4234/341;
            434%657;
            a = 12 + 21;
            b = 43 - 231;
            c = 32 * 4324;
            d = 4234/341;
            e = 34%534;
            func(34%534);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
        
    def test_wrong_int_type_1(self):
        input = """void testFunc()
        {
            a = 12[12];
        }"""
        expect = "Error on line 3 col 18: ["
        self.assertTrue(TestParser.checkParser(input,expect,259))   
        
    def test_wrong_int_type_2(self):
        input = """void testFunc()
        {
            a = !12;
        }"""
        expect = "Error on line 3 col 17: 12"
        self.assertTrue(TestParser.checkParser(input,expect,260))   
        
    def test_wrong_int_type_3(self):
        input = """void testFunc()
        {
            a = 12 && 342;
        }"""
        expect = "Error on line 3 col 19: &&"
        self.assertTrue(TestParser.checkParser(input,expect,261))
        
    def test_wrong_int_type_4(self):
        input = """void testFunc()
        {
            a = 12 || 5;
        }"""
        expect = "Error on line 3 col 19: ||"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_wrong_int_type_5(self):
        input = """void testFunc()
        {
            a = 12%1E2;
        }"""
        expect = "Error on line 3 col 19: 1E2"
        self.assertTrue(TestParser.checkParser(input,expect,263))
        
    def test_wrong_int_type_6(self):
        input = """void testFunc()
        {
            a = 12==1E2;
        }"""
        expect = "Error on line 3 col 20: 1E2"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_wrong_int_type_7(self):
        input = """void testFunc()
        {
            a = 12!=1E2;
        }"""
        expect = "Error on line 3 col 20: 1E2"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_float_type(self):
        input = """void testFunc()
        {
            f = -423.65423;
            12e3 + 21;
            43.E654 - 231;
            32.E-643 * 4324;
            4234/341.53;
            a = 12e3 + 21;
            b = 43.E654 - 231;
            c = 32.E-643 * 4324;
            d = 4234/341.53;
            func(4234/341.53);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_wrong_float_type_1(self):
        input = """void testFunc()
        {
            1e32[12];
        }"""
        expect = "Error on line 3 col 16: ["
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_wrong_float_type_2(self):
        input = """void testFunc()
        {
            !1e32;
        }"""
        expect = "Error on line 3 col 13: 1e32"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_wrong_float_type_3(self):
        input = """void testFunc()
        {
            1e32%3;
        }"""
        expect = "Error on line 3 col 16: %"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_wrong_float_type_4(self):
        input = """void testFunc()
        {
            1e32 == 3;
        }"""
        expect = "Error on line 3 col 17: =="
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_wrong_float_type_5(self):
        input = """void testFunc()
        {
            1e32 != 3;
        }"""
        expect = "Error on line 3 col 17: !="
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_wrong_float_type_6(self):
        input = """void testFunc()
        {
            1e32 && 3;
        }"""
        expect = "Error on line 3 col 17: &&"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_wrong_float_type_7(self):
        input = """void testFunc()
        {
            1e32 || 3;
        }"""
        expect = "Error on line 3 col 17: ||"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_string_type(self):
        input = """void testFunc()
        {
            a = "input string";
            func("param string");
            "input string";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_wrong_string_type_1(self):
        input = """void testFunc()
        {
            a = "abc"[12];
        }"""
        expect = "Error on line 3 col 21: ["
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_wrong_string_type_2(self):
        input = """void testFunc()
        {
            a = -"abc";
        }"""
        expect = "Error on line 3 col 17: \"abc\""
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_wrong_string_type_3(self):
        input = """void testFunc()
        {
            a = !"abc";
        }"""
        expect = "Error on line 3 col 17: \"abc\""
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_wrong_string_type_4(self):
        input = """void testFunc()
        {
            a = "abc"/"dsa";
        }"""
        expect = "Error on line 3 col 21: /"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_wrong_string_type_5(self):
        input = """void testFunc()
        {
            a = "abc"*"dsa";
        }"""
        expect = "Error on line 3 col 21: *"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_wrong_string_type_6(self):
        input = """void testFunc()
        {
            a = "abc"%"dsa";
        }"""
        expect = "Error on line 3 col 21: %"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_wrong_string_type_7(self):
        input = """void testFunc()
        {
            a = "abc"+"dsa";
        }"""
        expect = "Error on line 3 col 21: +"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_wrong_string_type_8(self):
        input = """void testFunc()
        {
            a = "abc"-"dsa";
        }"""
        expect = "Error on line 3 col 21: -"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_wrong_string_type_9(self):
        input = """void testFunc()
        {
            a = "abc">"dsa";
        }"""
        expect = "Error on line 3 col 21: >"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_wrong_string_type_10(self):
        input = """void testFunc()
        {
            a = "abc">="dsa";
        }"""
        expect = "Error on line 3 col 21: >="
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_wrong_string_type_11(self):
        input = """void testFunc()
        {
            a = "abc"<"dsa";
        }"""
        expect = "Error on line 3 col 21: <"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_wrong_string_type_12(self):
        input = """void testFunc()
        {
            a = "abc"<="dsa";
        }"""
        expect = "Error on line 3 col 21: <="
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_wrong_string_type_13(self):
        input = """void testFunc()
        {
            a = "abc"=="dsa";
        }"""
        expect = "Error on line 3 col 21: =="
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_wrong_string_type_14(self):
        input = """void testFunc()
        {
            a = "abc"!="dsa";
        }"""
        expect = "Error on line 3 col 21: !="
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_wrong_string_type_15(self):
        input = """void testFunc()
        {
            a = "abc"&&"dsa";
        }"""
        expect = "Error on line 3 col 21: &&"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_wrong_string_type_16(self):
        input = """void testFunc()
        {
            a = "abc"||"dsa";
        }"""
        expect = "Error on line 3 col 21: ||"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_arr_type(self):
        input = """void testFunc()
        {
            abcde[123];
            -abcde[123];
            !abcde[123];
            arr1[123]/arr2[123];
            arr1[123]*arr2[123];
            arr1[123]%arr2[123];
            arr1[123]+arr2[123];
            arr1[123]-arr2[123];
            arr1[123]>arr2[123];
            arr1[123]>=arr2[123];
            arr1[123]<arr2[123];
            arr1[123]<=arr2[123];
            arr1[123]==arr2[123];
            arr1[123]!=arr2[123];
            arr1[123]&&arr2[123];
            arr1[123]||arr2[123];
            a = arr1[123];
            a = arr1[123+123*321/4324 + arr[21] + func1(abc) + func2(arr[1]) * func3(arr)[13]];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291)) 

    def test_wrong_arr_type_1(self):
        input = """void testFunc()
        {
            a = arr[1][5];
        }"""
        expect = "Error on line 3 col 22: ["
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_wrong_arr_type_2(self):
        input = """void testFunc()
        {
            a = arr[1>2];
        }"""
        expect = "Error on line 3 col 21: >"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    #arr pointer type true case already test in decl func
    def test_wrong_arr_pnt_type_1(self):
        input = """void[] testFunc()
        {
        }"""
        expect = "Error on line 1 col 4: ["
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_wrong_arr_pnt_type_2(self):
        input = """int[12] testFunc()
        {
        }"""
        expect = "Error on line 1 col 4: 12"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_wrong_arr_pnt_type_3(self):
        input = """int[] testFunc(void a[])
        {
        }"""
        expect = "Error on line 1 col 15: void"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_wrong_arr_pnt_type_4(self):
        input = """int[] testFunc(string a[123])
        {
        }"""
        expect = "Error on line 1 col 24: 123"
        self.assertTrue(TestParser.checkParser(input,expect,297))
























#Add some missing testcase
    def test_wrong_decl_arr_invalid_size_5(self):
        input = """string abdffre["true"];"""
        expect = "Error on line 1 col 15: \"true\""
        self.assertTrue(TestParser.checkParser(input,expect,395))

    def test_wrong_decl_func_invalid_type_3(self):
        input = """ int[3] func(){}"""
        expect = "Error on line 1 col 5: 3"
        self.assertTrue(TestParser.checkParser(input,expect,396))

    def test_wrong_decl_invalid_variable_2(self):
        input = """int abdffre[123];
                    string badgdfa()
                    {
                        boolean 123abcde;
                    }
                    """
        expect = "Error on line 4 col 32: 123"
        self.assertTrue(TestParser.checkParser(input,expect,397))

    def test_wrong_decl_invalid_list_variable(self):
        input = """int abdffre[123],abe,asd,;"""
        expect = "Error on line 1 col 25: ;"
        self.assertTrue(TestParser.checkParser(input,expect,398))

    def test_wrong_decl_invalid_variable_1(self):
        input = """int abdffre[123];
                    string badgdfa()
                    {
                        boolean int,abcde,asda;
                    }
                    """
        expect = "Error on line 4 col 32: int"
        self.assertTrue(TestParser.checkParser(input,expect,399))
