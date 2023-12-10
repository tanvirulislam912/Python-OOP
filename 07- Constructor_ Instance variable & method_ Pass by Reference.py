
class Cat:

    def __init__(self, color, action):
        self.color= color
        self.action= action

    def view(self):
        print(self.color, "cat is", self.action)

    def compare(self, ct):                                  #compare two cats action
        if self.action == ct.action:
            print("Both cats are", self.action)
        else:
            print("They are different")    

c1= Cat("White", "jumping")
c2= Cat("Brown", "sitting")

c1.view()
c2.view()

c1.compare(c2)                                         #pass by reference
