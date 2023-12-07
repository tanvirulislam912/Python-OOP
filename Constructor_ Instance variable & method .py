class Car:
    def __init__(self, name, model):
        self.name= name                    #instance variable
        self.model_year= model             #instance variable
        self.wheel= 4                      #instance variable

    def view(self):                            #instance method
        print("The model year of this", self.name, "is",self.model_year)   
        print("It is a ", self.wheel, "wheel car")  

c1= Car("BMW", 2016)    
c2= Car("AUDI", 2018)    

c2.wheel= 6
c1.view()   
c2.view()   

print(c1)
print(c2)