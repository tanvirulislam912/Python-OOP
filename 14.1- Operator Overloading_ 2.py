n1 = 15
n2 = 25

print(n1 + n2)

print(n1.__add__(n2))

print(type(n1))
print(type(n2))


print("###################################")

class data:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x


num1 = data(10)
num2 = data(20)
str1 = data('cse')
str2 = data('111') 

print(num1 + num2)       #num1.__add__(num2)
print(str1 + str2)


print("###################################")


class House:
    def __init__(self, w, d):
        self.window = w
        self.door = d

    def view(self):
        print("The house has ", self.window, "windows and ",
              self.door, "doors")
        

    def __add__(self, other):
        new_window = self.window + other.window
        new_door = self.door + other.door   
        obj = House(new_window, new_door)
        return obj
        # return "New house has "+ str(new_window) + " windows and " + str(new_door) +  " doors" 
                

        
h1 = House(6,2)
h2 = House(4,1)
h1.view()
h2.view()  
h3 = h1 + h2                      #h1.__add__(h2)
h3.view()
# print(h1 + h2)                    #h1.__add__(h2)

