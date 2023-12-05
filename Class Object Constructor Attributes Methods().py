'''Class Objects Constructor Attributes Methods()'''


# class Student:
#     pass

# #variable = class_name()
# s1 = Student()
# print(s1)



class Student:

    def __init__(self,name, Id):                       #Constructor Created
        # print(self)
        self.name = name                                #Instance Variable  
        self.Id = Id
        # print("A student object created")
  
    def details(self):                                  #Instance Method
        print("Name:", self.name, "Id:", self.Id)                                  
         
            
#variable = class_name()
s1 = Student("Kobbla", 23)
s2 = Student("Habla", 34)

s1.Id = 67
s1.details()
s2.details()
s1.details()
s2.details()

# print(s1.Id) #23

# s1.Id = 33
# print(s1.Id) #33



# print(s1.name)
# print(s2.name)
# print(s2.Id)


# print('s1',s1)
# print('s2',s2)        

      
        