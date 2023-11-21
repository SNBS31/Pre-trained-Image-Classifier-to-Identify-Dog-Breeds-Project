# Now transposing our given data from a 4-by-3 matrix to a 3-by-4 matrix,
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
print(type(data))
data_transpose = tuple(zip(*data)) # i.e, maintaining it as a tuple, after the unzipping modification

print(data_transpose)