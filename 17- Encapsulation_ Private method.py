class Student:

    def __init__(self, name, Id):
        self.name = name              #instance variable
        self.__Id = Id                #public instace variable

    def details(self):                 #instance method
        print("Name:", self.name, "ID:", self.__Id)
        self.__method()

    def __method(self):
        print("private method executed")


s1 = Student("Bob", 11)
s2 = Student("Carol", 24)

#s1.__method()
s1.details()