name = 'Jim'
student = name
name = "Tim"
#print(name)
#print(student)

# Note:Remember, strings are immutable. Hence, doesn't affect the above variables

# Now for mutable lists,
scores = ["B","C","A","D","B","A"]
grades = scores
print(scores)
print(grades)
scores[3] = "B"
print(scores)
print(grades)
# As seen from the displayed results,both variables have been affected