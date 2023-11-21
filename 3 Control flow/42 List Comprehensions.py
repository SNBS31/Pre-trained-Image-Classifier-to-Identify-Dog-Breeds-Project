# list comprehension = a way of creating a new list, using but less syntax

squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)    

#Now Using the List Comprehension method,
squares = [i*i for i in range(1,11)]
print(squares)