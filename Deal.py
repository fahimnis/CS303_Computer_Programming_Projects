#  File: Deal.py
#  Description: HW 10
#  Student's Name: Fahim N Islam
#  Student's UT EID:
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created:03/25/20
#  Date Last Modified:03/25/20

import random

wins = [ ]

def roll(n):

    return random.randint(1,n)

def runOneTrial():

    prize = roll(3)
    guess = roll(3)

    view = 1

    while view == prize or view == guess:
        view = roll(3)

    newGuess  = 1

    while newGuess == view or newGuess == guess:
        newGuess = roll(3)


    print('{:^5d}{:2s}{:^5d}{:2s}{:^5d}{:7d}{:3s}'.format(prize,'  ',guess ,'  ',view,newGuess,'   '))

    if newGuess == prize:
        return('win')
    
    
    if newGuess != prize:
        return('lose')

def Deal():


    trials = int(input('How many trials do you want to run? '))

    print("")
    
    print('{:7s}{:7s}{:6s}{:9s}'.format('Prize','Guess' ,'View','New Guess'))

    for i in range(1,trials+1):

        result = runOneTrial()

        if result == 'win':

            wins.append(result)

    winprob = len(wins)/trials
    loseprob = 1 - winprob

    print('')
    print('Probability of winning if you switch =',winprob)
    print('Probability of winning if you do not switch =',loseprob)

            
Deal()
        


        

    
    
    

