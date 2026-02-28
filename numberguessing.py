import random
random_number = random.randint(1,100) #choosing random number
guesses = 0
while True:
    try:
        user_number = input('I am thinking of a number from 1 to 100. Guess what it is! (Enter "exit" to quit.) ')
        if user_number == 'exit':
            ('You gave up after ' + str(guesses) + ' guesses. The answer was ' + str(random_number))
            break
        int(user_number)
        difference = int(random_number) - int(user_number) #used to measure whether guess was higher or lower
        if int(user_number) > 100 or int(user_number) < 1:
            print('Enter an integer in the range 1-100. ')
        else:
            if difference == 0: #correct guess
                print('Congratulations! You guessed the number, ' + str(random_number) + '. And it only took you ' + str(guesses) + ' tries!')
                break
            if difference < 0: #guess was too low
                print('Lower.')
                guesses = guesses + 1
            if difference > 0: #guess was too high
                print('Higher.')
                guesses = guesses + 1
    except ValueError:
        print('Please enter a valid whole number. ') #just in case user enters bad input