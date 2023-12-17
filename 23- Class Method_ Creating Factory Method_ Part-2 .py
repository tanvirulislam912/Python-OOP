class Student:
    uni_name = "EDU"

    def __init__(self, name, Id):      #constructor
        self.name  = name
        self.__Id = Id

    def details(self):                #instance method
        print("Name: ", self.name, "Id:", self.__Id,
              Student.uni_name)
        

    @classmethod
    def up_uni_name(cls, u_name):
        cls.uni_name = u_name  

    @classmethod
    def from_string(cls, info):
        name, Id = info.split('-')
        obj = cls(name, Id)
        return obj
        


s1 = Student("Bob", 11)
s2 = Student.from_string("Carol-22")

print("s1:", s1)
print("s2:", s2)

s1.details()
s2.details()

