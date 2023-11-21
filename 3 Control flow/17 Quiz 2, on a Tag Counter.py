#Here, we're counting/filtering out(hence Conditioning required) but XML tags from a list of strings, using along the for loop

tokens = ['<greeting>', 'Hello World!', '</greeting>']
# We'll keep the number of tags using "count" to select from the first to the last element
count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
        
print(count)        

