# NOTE that we want to also know here the number of objects, which aren't fruits
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']


for object, count in basket_items.items():
    if object in fruits:
        fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}. There are {} objects that are not fruits.".format(fruit_count,not_fruit_count))            