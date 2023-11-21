f = open('some_file.txt', 'r') #"r" for in read mode
file_data = f.read()
f.close()

print(filea_data)

f = open('another_file.txt', 'w') #Is the file wasn't created b4, python will automatically create it for you through this command
f.write('Hello World!')
f.close() #Always close at every end, for assurance sake