class Student:
    def __init__(self, name, Id):
        self.name = name
        self.Id = Id

    def details(self):
        print("Name:", self.name, "Id:", self.Id)

class CSEStudent(Student):
    def __init__(self, name, Id, labs):
        super().__init__(name, Id)
        self.no_of_labs= labs
         
    def cry(self):
        print("CSE student is crying because of",
              self.no_of_labs, "labs" )
        

class BBAStudent(Student):
    # def __init__(self, name, Id):
    #     self.name = name
    #     self.Id = Id
 
    def party(self):
        print("All day party")     


s1 = CSEStudent("Bob", 11 ,3)
s2 = BBAStudent("Carol", 36)

s1.details()
s2.details()

s1.cry()
s2.party()

# print(help(s1))
# print(help(s2))
