class data:
    def __init__(self, x):
        self.x= x

    # adding two objects
    def __add__(self, other):
        return self.x + other.x    
    
num1 = data(10)  
num2 = data(20)  
str1 = data('cse')
str2 = data('111')
  
print(num1 + num2)          #num1. __add__(num2) 
print(str1  + str2)         #str1. __add__(str2) 


print("###########################################")

class data:
    def __init__(self, x):
        self.x= x

    
    def __gt__(self, other):
        if(self.x > other.x):
            return True
        else:
            return False
    
num1 = data(10)  
num2 = data(20)  

if (num1 > num2):                  #num1. __gt__(num2) 
    print("num1 is greater than num2")
else:
    print("num2 is greater than num1")   
  


print("###########################################")


class data:
    def __init__(self, x):
        self.x= x

    
    def __lt__(self, other):
        if(self.x < other.x):
            return "num1 is less than num2"
        else:
            return "num2 is less than num1"
    
num1 = data(10)  
num2 = data(20)  
print(num1 < num2)           #num1. __lt__(num2) 
           
   
 
  
print("###########################################")


class data:
    def __init__(self, x):
        self.x= x

    
    def __eq__(self, other):
        if(self.x == other.x):
            return "Both are equal"
        else:
            return "Not equal"
    
num1 = data(10)  
num2 = data(100)  
print(num1 ==  num2)           #num1. __eq__(num2) 
           
   