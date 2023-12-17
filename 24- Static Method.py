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

    @staticmethod
    def check_department(Id):
        if Id[3:5] == "01" : print("CSE")
        elif Id[3:5] == "41" : print("CS")



Student.check_department("14341007")

s1 = Student("Bob", 11)
s2 = Student("Carol", 22)

print("s1:", s1)
print("s2:", s2)

s1.details()
s2.details()

Student.check_department("15301007")



