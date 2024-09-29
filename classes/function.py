from os.path import dirname, join
from classes.case import CaseDefinition
from classes.value import SimpleValue, ComplexValue, PointerValue
from classes.stub import StubDefinition
from classes.helper import Helper

class FunctionDefinition:
    def __init__(self, parent, name, parameters, cases, stubs=None):
        self.parent = parent
        self.name = name
        self.parameters = parameters
        self.cases = cases
        self.stubs = stubs
        self.counterSpec = 1
        self.test_output = ''
        self.counterRes = 2
        self.helper = []

    def specIntroduction(self, desc)->str:
        output="/*\n"
        output+="This test case checks the behaviour of the "+self.name+" function in case "+desc+".\n\n"
        output+="{Test Specification}\n\n"
        return output
    
    def writeIndex(self, index):
        return str(index) if index>9 else "0"+str(index)

    def writeTestStubExpected(self, case):
        self.test_output+="\n\nvoid UT_Test_"+ self.name+"_TC_"+ self.writeIndex(self.cases.index(case))+"(){\n"
        if self.stubs:
            self.test_output+="  /* Functions called check */ \n"
            for stub in self.stubs:
                self.test_output+="  CPPTEST_EXPECT_NCALLS(\""+stub.stubFuncName+"\", "+str(stub.stubValue)+");\n"

    def writeExpectedResults(self, returnVal):
         output="\n\n{Expected Results} Expected result is Passed\n\n"
         output += "  1. "+self.name+" function returns "+returnVal+".\n"
         self.counterRes+=1
         return output
    
    def writeEndofSpec(self):
        output = "  "+str(self.counterSpec)+". Call "+self.name+" function with the following arguments: \n"
        for par in self.helper:   
            if par.value_par.__class__.__name__ == 'str' and "*" in par.value_par:
                output+= "  - " + par.name +" = pointing to the "+ par.name+"_example\n"
            else:
                output+= "  - " + par.name +" = "+ str(par.value_par)+"\n"
        output+="  "+str(self.counterSpec)+". Check expected results.\n"
        return output
    
    def writeTestParam(self):
        counter =1
        output = ""
        for par in self.helper:   
            output += "  /* Initializing argument "+str(counter)+" */\n" 
            if par.value_par.__class__.__name__ == 'str' and "*" in par.value_par:
                output+="  "+par.type_par.replace('*', '')+" = "+par.name+"_example;\n"
                output += "  "+par.type_par+" test_"+par.name+" = "+ par.name+"_example;\n"
            else:
                output += "  "+par.type_par+" test_"+par.name+" = "+ str(par.value_par)+";\n"
            counter+=1
        return output


    def interpret(self, output):
        this_folder = dirname(__file__)
        with open(join(this_folder, output), 'a') as file:
            for case in self.cases:
                self.writeTestStubExpected(case)
                file.write(self.specIntroduction(case.description))
                if self.parameters:
                    for param in case.parValues:
                        same_param = self.parameters[case.parValues.index(param)]
                        print("*************** "+same_param.name)
                        self.helper.append(Helper(same_param.name, same_param.type, param))
                        if isinstance(param, ComplexValue) or isinstance(param, PointerValue):
                            file.write(param.interpretSpecification(same_param.name, same_param.type, self.counterSpec))
                            self.counterSpec+=1 
                stubExcpected = ''
                self.test_output+=self.writeTestParam()
                for stub in self.stubs:
                    file.write("  "+str(self.counterSpec)+". Stub function "+stub.stubFuncName+"\n")
                    self.counterSpec+=1
                    self.test_output+="  CPPTEST_REGISTER_STUB_CALLBACK(\""+stub.stubFuncName+"\", &"+stub.stubCallback+");\n"
                    stubExcpected ="  "+str(self.counterRes)+". Function "+ stub.stubFuncName +" is called "+str(stub.stubValue)+ " time(s).\n"
                    self.counterRes+=1
                file.write(self.writeEndofSpec())
                file.write(self.writeExpectedResults(case.result))
                file.write(stubExcpected)
                self.test_output+= "\n  /* Tested function call */\n"
                self.test_output+= "  TtErrorType _return  = "+self.name+"("
                for index, param in enumerate(self.parameters):
                    self.test_output+="test_"+param.name
                    if index != len(self.parameters) - 1:
                        self.test_output+=","
                self.test_output+=");\n"
                self.test_output+="  /* Post-condition check */\n"
                self.test_output+="  CPPTEST_ASSERT_UINTEGER_EQUAL("+case.result+", _return);\n}\n\n"
                file.write("*/\n")
                file.write(self.test_output)
                self.test_output=''
                self.counterRes=1
                self.counterSpec=1
                self.helper = []
        



 