# Python Inheritence syntax

# class BaseClass:
#     Body of base class
        
# class DerivedClass(BaseClass):
#         Body of derived Class        



print("Single Inheritence: ")

class ParentClass:                    #Base Class
    def method1(self):
        print("This method1 is in ParentClass.")
    def method2(self):
        print("This method2 is in ParentClass.")   


class ChildClass(ParentClass):         #Derived Class
    def method3(self):
        print("This method3 is in ChildClass.")


ch1 = ChildClass()                     #Object of ChildClass
ch1.method1()
ch1.method2()
ch1.method3()


            