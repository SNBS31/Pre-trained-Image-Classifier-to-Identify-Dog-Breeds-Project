# if points <= 50:
#     result = "Congratulations! You won a wooden rabbit!"
# elif points <= 150:
#     result = "Oh dear, no prize this time."
# elif points <= 180:
#     result = "Congratulations! You won a wafer-thin mint!"
# else:
#     result = "Congratulations! You won a penguin!"

# We'll do the entire above now, using Truth Values

points = 237
prize = None

if points <= 50:
    prize = 'wooden rabbit'
elif 151 <= points <= 180: #The entire two-side interval here to avoid clashing the point mark with no prize
    prize = 'wafer-thin mint'
elif points >= 181:  
    prize = 'penguin'
    
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."   
    
print(result)               