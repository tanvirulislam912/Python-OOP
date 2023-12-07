class Dog:
    def __init__(self, name, color):
        self.name= name
        self.color= color

    def updated_color(self, color):
        self.color= color    

    def poke(self):                  #details
        print(self.color, self.name, "is smiling")

d1= Dog("rover", "Brown")
d2= Dog("tomy", "White")


d1.poke()
d1.updated_color("Black")
d1.poke()
print(d1.__dict__)               #Build in dictionary
print(dir(d1))                   #Build in function


d2.poke()
d2.updated_color("Red")
d2.poke()
print(d2.__dict__)                #Build in dictionary
print(dir(d2))                    #Build in function


