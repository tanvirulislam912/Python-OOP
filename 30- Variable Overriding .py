class Animal:

    def __init__(self, name):
        self.name = name
        self.color = "white"

    def eat(self):
        print(self.color, self.name, "is eating") 


class Dog(Animal):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def bark(self):
        print(self.color, self.name, "is barking") 


d1 = Dog("Rover", "Brown")
# print(d1.__dict__)
d1.bark()
d1.eat()               
