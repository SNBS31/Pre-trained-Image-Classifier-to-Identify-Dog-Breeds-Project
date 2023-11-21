def cylinder_volume(height, radius=5):
    pi = 3.14159
    return pi * radius**2 * height

print(cylinder_volume(10,5))
print(cylinder_volume(10))
print(cylinder_volume(10,7))
print(cylinder_volume(radius=7, height=10)) 