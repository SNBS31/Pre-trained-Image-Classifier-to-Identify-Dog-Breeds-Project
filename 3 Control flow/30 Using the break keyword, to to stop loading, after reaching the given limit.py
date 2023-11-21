manifest = [('bananas', 15), ('mattresses', 34), ('dog kennels', 42), ('machine',120), ('cheeses', 5)]

weight = 0 # Weight should start from zero always, so that we can start adding from scratch
items = []
for cargo_name, cargo_weight in manifest: #Meaning these two respective variables represent them tuple items inside the variable "manifest" respectively
    print('Current weight: {}'.format(cargo_name,cargo_weight)) #To just help see where the problem lies
    if weight >= 100: # Meaning the point where the weight has bypassed 100(i.e in this case from 91(of the previous loop) to 211)
        print('breaking the loop now!') #To help.....
        break # Meaning it's but at the 211 weight mark that the loop stops 
    else:
        print(' adding {} ({})'.format(cargo_name,cargo_weight)) #To just help....
        items.append(cargo_name) #adding the name of the item 
        weight += cargo_weight   #adding along the item's weight
        
print('\nFinal Weight: {}'.format(weight))
print('\nFinal items: {}'.format(items))      
