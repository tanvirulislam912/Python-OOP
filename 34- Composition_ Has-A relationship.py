class Engine:
    def __init__(self, cc):
        self.capacity = cc

    def start(self):
        print("Engine Started")

    def stop(self):
        print("Engine Stopped")        


class Car:
    def __init__(self, name, cc):
        # super().__init__(cc)
        self.name = name
        self.engine = Engine(cc)     #Create Object

    def run(self):
        self.engine.start()
        # print(self.engine)
        print("Car is running")


c1 = Car("BMW", 2000)
c1.run()            
