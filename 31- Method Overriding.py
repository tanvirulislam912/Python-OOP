class A:
    def __init__(self):
        print("__init__ of class A")

    def method1(self):
        print("Olpo study")

    def method2(self):
        print("You will get all of my property and methods")


class B(A):
    def __init(self):
        print("__init__ of class B")

    def method1(self):
        super().method1()
        print("Always party")    

b1 = B()
b1.method1()
b1.method2()                        