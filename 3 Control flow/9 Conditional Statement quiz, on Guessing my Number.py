answer = 35
guess = 25

if guess < answer:
    result = 'Ooops! Your guess is too low.'
elif guess > answer:
    result = 'Ooops! Your guess is too high.'    
else:
    result = 'Nice! Your guess matched the answer!'
    
print(result)        