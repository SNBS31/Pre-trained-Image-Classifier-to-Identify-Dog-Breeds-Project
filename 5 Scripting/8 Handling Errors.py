while True:
    try:
        x = int(input('Enter your number: '))
        break
    except:
        print('Not a valid number Sir!')    
    finally:
        print('\nTake tour time and do it again\n')    