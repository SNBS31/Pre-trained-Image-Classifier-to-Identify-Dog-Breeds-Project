items = ['banana', 'mattresses', 'dog kennels', 
         'machine', 'cheeses']

weights = [15, 34, 42, 120, 5]

#print(list(zip(items,weight))) #Not necessary to convert to a list, but nice for proper presentation of results
# OR
for cargo in zip(items,weights): #As cargo represents each element in each of em tuples
    print(cargo[0], cargo[1])