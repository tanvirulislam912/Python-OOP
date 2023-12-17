class Student:
    uni_name = "EDU"

    def __init__(self, name, Id):
        self.name  = name
        self.__Id = Id

    def details(self):          #instance method
        print("Name: ", self.name, "Id:", self.__Id,
              Student.uni_name)
        

    @classmethod
    def up_uni_name(cls, u_name):
        # print("class method called")
        cls.uni_name = u_name  


# Student.up_uni_name("East Delta University")

        
s1 = Student("Bob", 11)
s2 = Student("Carol", 22)

s1.details()
s2.details()

Student.up_uni_name("East Delta University")

# s1.up_uni_name("East Delta University")


s1.details()
s2.details()

print(s1.__dict__)
print(s2.__dict__)
