class Prey:
    def flee(self):
        print("The animal is fleeing for it's life")
        
class Predator:
    def hunt(self):
        print("The animal is hunting for survival")
        
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit() #It's now we're creating our objects
hawk = Hawk()
fish = Fish() 

# rabbit.flee()
# hawk.hunt()  

fish.flee()
fish.hunt()             