# cities_in_F = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}
# cities_in_C = {key: round(value-32)*(5/9) for (key,value) in cities_in_F.items()}

# print(cities_in_C)

weather = {'New York':'snowing', 'Boston':'sunny', 'Los Angeles':'sunny', 'Chicago':'cloudy'}
sunny_weather = {key:value for (key,value) in weather.items() if value == 'sunny'}

print(sunny_weather)