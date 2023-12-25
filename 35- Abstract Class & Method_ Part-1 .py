from abc import ABC, abstractmethod


from abc import ABC, abstractmethod

class food (ABC):
    @abstractmethod
    def taste(self):
        pass

class pizza(food):
    def taste(self):
        print('Pizza is delicious')
    def size(self):
        print('12 inch pizza')

p = pizza()
p.taste()
p.size() 