# Here, we're trying to make the result such that the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast): # Since character now represents cast(each of it's items now having a unique number or index),
    cast[i] = character + " " + str(heights[i])
    
print(cast)    