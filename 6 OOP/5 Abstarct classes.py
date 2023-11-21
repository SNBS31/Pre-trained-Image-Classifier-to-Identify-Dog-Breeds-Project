class Vehicle:
    def go(self): #The abstract method
        pass
    
class Car(Vehicle):
    def go(self):
        print("Drive the car")
        
class Motorcycle(Vehicle):
    def go(self):
        print("Ride the motorcycle")      
        
vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go() #Gives nothing, since an object wasn't created here
car.go()
motorcycle.go()             