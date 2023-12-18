class Animal:                                           #parent class / base class / super class

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")



class Dog(Animal):                                     #child class / derived class / sub class

    def bark(self):
        print(self.name, "is barking")

                            
a1 = Animal("Jack")
d1 = Dog("Rover")

d1.bark()
d1.eat()

a1.eat()
# a1.bark()


# isinstance(Object, ClassName)
print(isinstance( d1, Animal))


#issubclass(Class, ClassName)
print(issubclass(Dog, Animal))