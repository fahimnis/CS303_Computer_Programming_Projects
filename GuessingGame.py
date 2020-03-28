#  File: GuessingGame.py
#  Description: Hw 7
#  Student's Name: Fahim Noor Islam
#  Student's UT EID: fni66
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created:2/23/20
#  Date Last Modified:2/26/20


#    Disclaimer: Please don't be confused about my comments counting trys. I understand
#    that all the ttries can happen within one loop
#    the purpose of repeating the while statements was to accomodate for the event
#    where the user switches between low and high values with each try.
#    I only had to inlcude the loop 10 times because the user can only switch values 10 times. 


def GuessingGame():

    #set up game variables

    secret_number = 5946
    counter = 0

    #take input from user

    print('Welcome to the guessing game.  You have ten tries to guess my number.')
    guess = int(input('Please enter your guess: '))

    #repeat until guess is within range

    while guess <= 0 or guess > 9999:

        print('Your guess must be between 0001 and 9999.')
        guess = int(input('Please enter a valid guess: '))


    if guess == secret_number:

        print("That's correct!")
        print('Congratulations! You guessed it on the first try!')

# FIRST TRY

    while guess < secret_number:

        counter += 1

        if counter == 10:

            print('Guesses so far:',counter)
            print('Game over: you ran out of guesses.')
            break

        elif counter <= 9:

            print('Your guess is too low.')
            print('Guesses so far:',counter)
            guess = int(input('Please enter your guess: '))

    while guess <= 0 or guess > 9999:

        print('Your guess must be between 0001 and 9999.')
        guess = int(input('Please enter a valid guess: '))

#SECOND TRY
            
    while guess > secret_number:

        counter += 1

        if counter == 10:

            print('Guesses so far:',counter)
            print('Game over: you ran out of guesses.')
            break

        else:

            print('Your guess is too high.')
            print('Guesses so far:',counter)
            guess = int(input('Please enter your guess: '))

    while guess <= 0 or guess > 9999:

        print('Your guess must be between 0001 and 9999.')
        guess = int(input('Please enter a valid guess: '))
            
# THIRD TRY

    while guess < secret_number:

        counter += 1

        if counter == 10:

            print('Guesses so far:',counter)
            print('Game over: you ran out of guesses.')
            break

        elif counter <= 9:

            print('Your guess is too low.')
            print('Guesses so far:',counter)
            guess = int(input('Please enter your guess: '))

    while guess <= 0 or guess > 9999:

        print('Your guess must be between 0001 and 9999.')
        guess = int(input('Please enter a valid guess: '))


#FOURTH TRY

    while guess > secret_number:

        counter += 1

        if counter == 10:

            print('Guesses so far:',counter)
            print('Game over: you ran out of guesses.')
            break

        else:

            print('Your guess is too high.')
            print('Guesses so far:',counter)
            guess = int(input('Please enter your guess: '))

    while guess <= 0 or guess > 9999:

        print('Your guess must be between 0001 and 9999.')
        guess = int(input('Please enter a valid guess: ')) 

#FIFTH TRY

    while guess < secret_number:

        counter += 1

        if counter == 10:

            print('Guesses so far:',counter)
            print('Game over: you ran out of guesses.')
            break

        elif counter <= 9:

            print('Your guess is too low.')
            print('Guesses so far:',counter)
            guess = int(input('Please enter your guess: '))

    while guess <= 0 or guess > 9999:

        print('Your guess must be between 0001 and 9999.')
        guess = int(input('Please enter a valid guess: '))

#SIXTH TRY

    while guess > secret_number:

        counter += 1

        if counter == 10:

            print('Guesses so far:',counter)
            print('Game over: you ran out of guesses.')
            break

        else:

            print('Your guess is too high.')
            print('Guesses so far:',counter)
            guess = int(input('Please enter your guess: '))

    while guess <= 0 or guess > 9999:

        print('Your guess must be between 0001 and 9999.')
        guess = int(input('Please enter a valid guess: '))

#SEVENTH TRY

    while guess < secret_number:

        counter += 1

        if counter == 10:

            print('Guesses so far:',counter)
            print('Game over: you ran out of guesses.')
            break

        elif counter <= 9:

            print('Your guess is too low.')
            print('Guesses so far:',counter)
            guess = int(input('Please enter your guess: '))

    while guess <= 0 or guess > 9999:

        print('Your guess must be between 0001 and 9999.')
        guess = int(input('Please enter a valid guess: '))

#EIGHTH TRY

    while guess > secret_number:

        counter += 1

        if counter == 10:

            print('Guesses so far:',counter)
            print('Game over: you ran out of guesses.')
            break

        else:

            print('Your guess is too high.')
            print('Guesses so far:',counter)
            guess = int(input('Please enter your guess: '))

    while guess <= 0 or guess > 9999:

        print('Your guess must be between 0001 and 9999.')
        guess = int(input('Please enter a valid guess: '))

#NINTH TRY


    while guess < secret_number:

        counter += 1

        if counter == 10:

            print('Guesses so far:',counter)
            print('Game over: you ran out of guesses.')
            break

        elif counter <= 9:

            print('Your guess is too low.')
            print('Guesses so far:',counter)
            guess = int(input('Please enter your guess: '))

    while guess <= 0 or guess > 9999:

        print('Your guess must be between 0001 and 9999.')
        guess = int(input('Please enter a valid guess: '))

#LAST TRY

    while guess > secret_number:

        counter += 1

        if counter == 10:

            print('Guesses so far:',counter)
            print('Game over: you ran out of guesses.')
            break

        else:

            print('Your guess is too high.')
            print('Guesses so far:',counter)
            guess = int(input('Please enter your guess: '))



    if guess == secret_number:

        counter += 1

        print("That's correct!")
        print('Congratulations! You guessed it in',counter,' guesses.')


GuessingGame()


