def population_density(population,land_area):
    return population/land_area

test1 = population_density(10,1)
expected_result = 10
print("expected result:{}, actual result:{}".format(expected_result,test1))