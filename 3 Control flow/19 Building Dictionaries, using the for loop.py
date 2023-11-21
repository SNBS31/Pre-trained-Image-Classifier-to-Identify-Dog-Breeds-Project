book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}

# METHOD1
# for word in book_title:
#     if word not in word_counter:
#         word_counter[word] = 1 #Since we start counting each word appeareance from 1, and never zero from normal indexing
#     else:
#         word_counter[word] += 1
        
# print(word_counter)        

# METHOD2    
for word in book_title:
    word_counter[word] = word_counter.get(word,0)+1
    
print(word_counter)    