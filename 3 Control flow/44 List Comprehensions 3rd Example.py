# squares = []

# for x in range(9):
#     squares.append(x**2)
# print(squares)

#Now using List Comprehensions,
squares = [x**2 for x in range(9)]
print(squares)    

#We can even filter out again, that the results must be even
#i.e
squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)

#But if we want to observe else within our list comprehension,
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)] 
print(squares)