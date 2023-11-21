elements = {'hydrogen': {'number': 1,
                        'weight': 1.00794,
                        'symbol': 'H'},
            'helium': {'number': 2,
                       'weight': 4.002602,
                       'symbol': 'He'}}

# print(elements['helium'])
# print(elements.get('unobtainium',"There's no such element!"))
# print(elements['helium']['weight'])

# Now to add another element in the above mix,
oxygen = {'number':8, 'weight':15.999, 'symbol':'O'}
elements['Oxygen'] = oxygen

#print(elements)
print('elements = ', elements)