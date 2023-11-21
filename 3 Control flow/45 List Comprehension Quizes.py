#Now filtering out the first names all in lower case form,
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names] #Since we have to split() first,b4 precising our location
print(first_names)

#Quiz 2: First 20 multiples of 3
multiples_3 = [x*3 for x in range(1,21)] #Since zero ain't a multiple of 3,as a number's multiple starts with it's own number
print(multiples_3)

#Quiz 3: That from atleast the score of 65, that student has passed
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
passed = [name for name,score in scores.items() if score >= 65]
print(passed)