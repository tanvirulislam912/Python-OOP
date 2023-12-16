
print('Instance Method :')

class myClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    #instance method
    def avg(self):
        print((self.a + self.b) /2)

m1 = myClass(20, 30)
m1.avg()      




print('Class Method :')

class Employee:
    org_name = 'Google'
    def __init__(self, name):
        self.name = name

    @classmethod
    def info(cls):
        return cls.org_name

print(Employee.info())    




print('Static Method :')

class Employee:
    org_name = 'Google'
    def __init__(self, name):
        self.name = name

    @staticmethod
    def detail():
        print("This is an Employee Class")

Employee.detail()


print("############################################################################")
print("Types of methods: ")

class MyClass:
    def method(self):
        print(self, 'Instance method called')


    @classmethod
    def class_method(cls):
        print(cls, 'class method called')


    @staticmethod
    def static_method():
        print("static method called")
        
                 