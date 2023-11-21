def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius**2

# METHOD1:Using the funtion three times,
cylinder_volume(10,3)
cylinder_volume(11,4)
cylinder_volume(12,5)

# METHOD2:Writing the cylinder volume formula three times
pi = 3.14159
10 * pi * 3**2
11 * pi * 4**2
12 * pi * 5**2

#hence, the first method is easiear, since we don't have to keep on writing formulas again and again
