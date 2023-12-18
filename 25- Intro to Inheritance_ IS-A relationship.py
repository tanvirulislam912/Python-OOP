# Python Inheritence syntax

# class BaseClass:
#     Body of base class
        
# class DerivedClass(BaseClass):
#         Body of derived Class        

print("#########################################################################")           


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


print("#########################################################################")           

print("Multilevel Inheritence: ")

class ParentClass:                         #Base Class
    def method1(self):
        print("This method1 is in ParentClass.")

class ChildClass1 (ParentClass):             #Derived Class1
    def method2(self):
        print("This method2 is in ChildClass1.")

class ChildClass2 (ChildClass1):              #Derived Class2
    def method3(self):
        print("This method3 is in ChildClass2.")


ch1 = ChildClass2()                          #Object of ChildClass2
ch1.method1()
ch1.method2()
ch1.method3()




print("#########################################################################")           

print("Hierarchical Inheritence: ")

class ParentClass:                           #Base Class 1
    def method1(self):
        print("This method1 is in Parent Class.")

class ChildClass1 (ParentClass):              #Derived Class 1
    def method2(self):
        print("This method2 is in Child 1.")

class ChildClass2 (ParentClass):               #Derived Class 2
    def method3(self):
        print("This method3 is in Child 2.")


ch1 = ChildClass1()                            #Object of ChildClass1
ch2 = ChildClass2()                            #Object of ChildClass2
ch1.method1()
ch2.method1()




print("#########################################################################")           

print("Multiple Inheritence: ")

class ParentClass1:                           #Base Class 1
    def method1(self):
        print("This method1 is in ParentClass1.")

class ParentClass2:                            #Base Class 2
    def method2(self):
        print("This method2 is in ParentClass2.")

class ChildClass(ParentClass1, ParentClass2):   #Derived Class
    def method3(self):
        print("This method3 is in ChildClass.")


ch1 = ChildClass()                            #Object of ChildClass                           
ch1.method1()
ch1.method2()
ch1.method3()




print("#########################################################################")           

print("Hybrid Inheritence: ")

class ParentClass:                           #Base Class 
    def method1(self):
        print("This method1 is in ParentClass.")

class ChildClass1(ParentClass):              #Derived Class 1
    def method2(self):
        print("This method2 is in ChildClass1.")

class ChildClass2(ChildClass1):              #Derived Class 2
    def method3(self):
        print("This method3 is in ChildClass2.")

class ChildClass3(ChildClass1):              #Derived Class 3
    def method4(self):
        print("This method4 is in ChildClass3.")                


ch1 = ChildClass3()                           #Object of ChildClass3                          
ch1.method1()
ch1.method2()





print("#########################################################################")           

print("Super: ")

class ParentClass:
    def feature1(self):
        print('feature1 is from ParentClass')

    def feature2(self):
        print('feature2 is from ParentClass')


class ChildClass(ParentClass):
    def feature3(self):
        super().feature1()
        print('feature3 is from ChildClass')
        super().feature2()


obj = ChildClass()
obj.feature3()        




print("#########################################################################")           

print("Method Overriding: ")


class ParentClass:
    def method1(self):
        print("method1 defined in parent class!")

class ChildClass(ParentClass):            #child class overriding the method of parent class        
    def method1(self):
        print("method1 defined in child class!!!!!!!") 


ch1 = ChildClass()
ch1.method1()               