num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0 # To count the number of times we're adding
list_sum = 0  # Since we start adding but from nothing
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): #i.e counting through the entire length, but ending after up to the first 5 numbers
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1
    
print("The number of the odd numbers added are {}".format(count_odd))
print("The sum from the addition was {}".format(list_sum))    