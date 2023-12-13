class Student:
    counter = 0                    #class or static variable
    def __init__(self, name, Id):
        self.name = name           #instance variable
        self.Id = Id
        Student.counter += 1

    def details(self):
        print("Name:",self.name, "ID:", self.Id)



print("Student Count",Student.counter)
s1 = Student("Bob", 11)
s2 = Student("Carol", 22)
s3 = Student("Mike", 33)


s1.details()
s2.details()
s3.details()
print("Student Count",Student.counter)



