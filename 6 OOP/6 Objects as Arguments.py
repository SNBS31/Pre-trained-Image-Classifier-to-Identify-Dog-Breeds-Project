class Car:
    color = None
    
def change_color(car,color): #A seperate class, which doesn't have to start with a capital letter, as the above function

    car.color = color
    
car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1, "red")
change_color(car_2, "blue")
change_color(car_3, "black")     

print(car_1.color)
print(car_2.color)
print(car_3.color)       