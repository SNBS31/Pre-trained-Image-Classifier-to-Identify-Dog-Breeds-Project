cities = ['New York', 'Chicago', 'Los Angeles', 'Miami']

# capitalized_cities = []
# for city in cities:
#     capitalized_cities.append(city.title())
    
# print(capitalized_cities)  

#The List Comprehension METHOD(i.e, the For Loop in 1step)
capitalized_cities = [city.title() for city in cities]  

print(capitalized_cities)