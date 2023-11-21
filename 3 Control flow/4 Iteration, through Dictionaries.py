cast = {
    'Jerry Seinfield': 'Jerry Seinfeld',
    'Julia Louis-Dreyfus': 'Elaine Benes',
    'Jason Alexander': 'George Costanza',
    'Michael Ricards': 'Cosmo Kramer'
}
print('Iteration through keys:')
for key in cast:
    print(key) #Overall code result same, if this line ain't there
    
print('\nIteration through keys and values:')    
for key, value in cast.items():
    print('Actor: {}  Role: {}'.format(key,value))
    