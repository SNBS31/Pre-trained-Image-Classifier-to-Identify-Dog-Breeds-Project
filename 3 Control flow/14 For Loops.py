cities = ['new york city','mountain view','chicago','los angeles']

# for city in cities:
#     print(city.title())
# print('Done!')    
    

Capitalized_cities = []

for city in cities:
    Capitalized_cities.append(city.title())
print(Capitalized_cities)    

#Now modifying our above list using the for loop,
# for index in range(len(cities)):
#     cities[index] = cities[index].title()
    
# When we modify a loop, it affects all it's elements as shown in the below example
# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2    
# print(numbers)    