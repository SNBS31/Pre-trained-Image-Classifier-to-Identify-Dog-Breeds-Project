items = ['bananas', 'mattresses', 'dog kennels',
         'machine', 'cheeses']

#Method1
# for i, item in zip(range(len(items)), items):
#     print(i, item)
    
#Method2(Enumerate), the simpler method
for i, item in enumerate(items): #Since we're talking about both the indexing(i) and item's elements(item)
    print(i, item)    