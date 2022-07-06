
import constant

from robot.libraries.BuiltIn import BuiltIn

class myLib():

    def __init__(self):
        print("...init...")
        constant.STORAGE["ENVIRONMENT"] = "TEST"

    def set_environment(self,ENVIRONMENT:str):
        constant.STORAGE["ENVIRONMENT"] = ENVIRONMENT.upper()
    
    def get_environment(self) -> str:
        return constant.STORAGE["ENVIRONMENT"]

    def set_platform(self,PLATFORM:str):
        constant.STORAGE["PLATFORM"] = PLATFORM.upper()
    
    def get_platform(self) -> str:
        return constant.STORAGE["PLATFORM"]

    def assign_to_preprod(self):
        if(constant.STORAGE["ENVIRONMENT"] == "PREPROD"):
            print("Test case run on Preprod")
        else:
            BuiltIn.skip(self,msg="Test skipped. Preprod assgined test cases cannot run on other environment.")
    
    def assign_to_test(self):
        if(constant.STORAGE["ENVIRONMENT"] == "TEST"):
            print("Test case run on Test")
        else:
            BuiltIn.skip(self,msg="Test skipped. Test assgined test cases cannot run on other environment.")

    def import_libraries(self,LIBRARY:str):
        BuiltIn.import_library(BuiltIn,LIBRARY,"")
    
    def import_variables(self,VARIABLE:str):
        BuiltIn.import_variables(BuiltIn,VARIABLE)
