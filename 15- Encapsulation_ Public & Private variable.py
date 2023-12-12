class Student:

    def __init__(self, name, Id):
        self.name = name     #public instance variable
        self.__Id = Id       #private instance variable

    def details(self):
        print("Name:", self.name, "ID:",self.__Id)


    def updt_ID(self, Id):
        if(Id>0):
            self.__Id = Id
        else:
            print("Invalid ID, enter id again")         

s1 = Student("Bob", 11)
s2 = Student("Carol", 24)

# s1.Id = 22

# s1.__Id = -66
# print(s1.__dict__)
# s1.updt_ID(-666)

s1.updt_ID(666)


s1.details()
s2.details()