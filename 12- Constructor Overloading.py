class Student:
    # def __init__(self, name, Id):
    #     self.name = name
    #     self.Id = Id

    # def __init__(self, name, Id, cg):    #Constructor overloading
    #     self.name = name
    #     self.Id = Id    
    #     self.CGPA = cg


#     def __init__(self, *info):
#         if len(info) == 3:    
#            self.name = info[0]
#            self.Id = info[1]   
#            self.CGPA = info[2]
#         elif len(info) == 2:    
#            self.name = info[0]
#            self.Id = info[1]   
#         elif len(info) == 1:    
#            self.name = info[0]
 
#         print("A student object created")
       
# s1 = Student("Carol", 33, 3.95)
# s2 = Student("Bod", 11)
# s3 = Student("Mike")       
# s4 = Student()


     def __init__(self, **info):
        if len(info) == 3:    
           self.name = info['name']
           self.Id = info['Id']   
           self.CGPA = info['CG']
        elif len(info) == 2:    
           self.name = info['name']
           self.Id = info['Id']   
        elif len(info) == 1:    
           self.name = info['name']
 
        print("A student object created")
       
s1 = Student(name="Carol", Id= 33, CG= 3.95)
s2 = Student(name= "Bod", Id= 11)
s3 = Student( Id= 11, name= "Bod")
s4 = Student(name= "Mike")    
s5 = Student()

