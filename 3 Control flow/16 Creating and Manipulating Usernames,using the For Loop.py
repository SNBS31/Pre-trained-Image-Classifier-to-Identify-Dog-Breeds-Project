names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

#That we have to copy the above list to the epmty list,then lower case the above elements,underscore them where them spaces are

for name in names:
    usernames.append(name.lower().replace(" ","_"))
    
print(usernames)    

#Now modifying these usernames using range,
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ","_")
    
print(usernames)    