fruit = ['orange', 'strawberry', 'apple', 'pear']
foods = ['apple', 'apple', 'pear', 'hummus', 'toast']

fruit_count = 0
for food in foods:
    if food not in fruit:
        print('Not a fruit')
        continue
    fruit_count += 1
    print('Found a fruit!')
    
print('Total fruit: ', fruit_count)    