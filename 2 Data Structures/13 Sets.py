# Normally, there are 785 responses from a certain online survey, from all countries in the world
#countries = ['Angola', 'Maldives', 'India', 'United States', 'India', 'Denmark', 'Sweden', 'Ghana', ... 777 more countries not displayed]
#country_set = set(countries)
#print(len(country_set)) # = 196 Since there are 196 countries in the world

my_list = [1,2,3,2,4,1,5]
new_list = list(set(my_list))

print(new_list)