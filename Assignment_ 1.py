

class Test3:
    def __init__(self):
        self.sum= 0
        self.y= 0

    def methodA(self):
        x= 2
        y= 3
        msg= [0]
        msg[0]= 3
        y= self.y + msg[0]
        self.methodB(msg, msg[0])
        x= self.y + msg[0]
        self.sum= x + y + msg[0] 
        print(x, y, self.sum)

    def methodB(self, mg2, mg1):
        x= 0
        self.y= self.y + mg2[0]
        x= x + 33 + mg1   
        self.sum= self.sum + x + self.y
        mg2[0]= self.y + mg1
        mg1= mg1 + x + 2
        print(x, self.y, self.sum)



t3 = Test3()
t3.methodA()
t3.methodA()

