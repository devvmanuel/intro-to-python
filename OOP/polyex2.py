class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def move(self):
            print("driving around")

class Plane:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def move(self):
            print("flying around")

class Motorbike:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def move(self):
        print("riding around")




#instance of our class

car = Car("toyota", "markx")
plane = Plane("boeing", "737")
bike = Motorbike("kawasaki","ninja450")



for i in (car, plane, bike):
    i.move()