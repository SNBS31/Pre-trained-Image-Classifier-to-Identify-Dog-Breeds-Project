cities = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}

desc_cities = {key: ('Warm' if value >= 40 else 'Cold') for (key,value) in cities.items()}

print(desc_cities)