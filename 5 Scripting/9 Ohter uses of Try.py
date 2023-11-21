while True:
    try:
        x = int(input('Enter a number '))
        break
    except ValueError: #To allow ctr+C, make us break out the loop if we can't get the right type of entry right
        print("That's not a valid number")
    finally:
        print('\nAttempted Input\n')    