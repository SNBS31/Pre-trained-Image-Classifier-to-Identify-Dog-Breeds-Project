class Animal:
    alive = True
    
    def eat(self):
        print("The animal is eating")
        
    def sleep(self):
        print("The animal is sleeping")  
        
class Rabbit(Animal):
    def run(self):
        print("The rabbit runs")
        
class Fish(Animal):
    def swim(self):
        print("The fish swims")
    
class Hawk(Animal):
    def fly(self):
        print("The hawk flies")      
        
rabbit = Rabbit() #Defining them objects(the child classes)
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.fly()

# rabbit.run()
# fish.swim()
# hawk.fly()



                        