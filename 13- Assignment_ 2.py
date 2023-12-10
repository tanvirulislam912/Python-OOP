class Student:
    def __init__(self, name, Id):
        self.name = name
        self.Id = Id

class dummy:
    def __init__(self):
        self.val = 0

    def detail(self, std):
        # print(std)
        # print(std.name)
        # print(std.Id)
        self.val = std



s1 = Student("Bob", 11)
# print(s1)
d1 = dummy()

# d1.detail(23)
# d1.detail("CSE")

# d1.detail(s1.name)              #pass by value
# d1.detail(s1.Id)                #pass by value

d1.detail(s1)                   #pass by reference
print(d1.val)

print(d1.val.name)         #Bob
print(d1.val.Id)           #11