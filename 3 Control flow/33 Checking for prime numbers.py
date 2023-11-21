check_prime = [26,39,51,53,57,79,85]

for num in check_prime:
    
# Since 2 is the first prime number as it divides both 1 and itself,
    for i in range(2,num):
## Since for each prime number, their % is never 0,
        if (num % i) == 0:
            print("{} ain't a prime number, since {} is a factor of it".format(num,i))        
            break
        
        if num == -1: # i.e, when the loop reaches the last possible given Prime Number
            print("{} IS a prime number".format(num))         
    