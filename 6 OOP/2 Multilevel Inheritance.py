class Organism:
    
    alive = True
    
class Animal(Organism):
    
    def eat(self):
        print("The animal is eating")
        
class Dog(Animal): 
    
    def bark(self):
        print("The barking from this dog can cause you to sharply respond to its stimuli")
       
       
dog = Dog()
print(dog.alive)      
dog.eat()     
dog.bark()