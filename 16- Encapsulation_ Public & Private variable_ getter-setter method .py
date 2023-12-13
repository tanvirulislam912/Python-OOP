class Student:

    def __init__(self, name, Id):
        self.name = name            #public instance variable
        self.__Id = Id              #private instance variable

    def details(self):
        print("Name:", self.name, "ID:",self.__Id)


    def set_ID(self, Id):
        if(Id>0):
            self.__Id = Id
        else:
            print("Invalid ID, enter id again")  

    def get_ID(self):
        return self.__Id  

    def set_name(self, name):
        self.name = name 

    def get_name(self):
        return self.name



s1 = Student("Bob", 11)
s2 = Student("Carol", 24)

s1.set_ID(55)
s2.set_ID(95)

print(s1.get_ID())
print(s2.get_ID())

s1.set_name('Mike')
s2.set_name('Hike')

print(s1.get_name())
print(s2.get_name())

s1.details()
s2.details()


