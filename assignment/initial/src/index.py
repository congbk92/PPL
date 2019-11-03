import fileinput

filename = 'test/ASTGenSuite.py'

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    count = 300
    for line in file:
        if line.find("self.assertTrue(TestAST.checkASTGen(input,expect,400))") != -1:
            print(line.replace("400",str(count)),end='')
            count +=1
        else:
            print(line,end='')