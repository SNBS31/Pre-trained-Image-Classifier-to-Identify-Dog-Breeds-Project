verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
#print(verse, "\n")

# Now we "spilt"(a method) our above verse, meaning we're coverting the above into a list
verse_list = verse.split()
#print(verse_list) 

# Now coverting our directly above list into a set that keeps soley unique elements,
verse_set = set(verse_list)
#print(verse_set)

#Now finding our length of our above container,
num_unique = len(verse_set)
print(num_unique)