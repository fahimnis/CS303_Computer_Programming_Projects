#  File: Initials.py
#  Description: Hw2
#  Student's Name: Fahim Noor Islam
#  Student's UT EID: fni66
#  Course Name: CS 313E 
#  Unique Number: 50180
#
#  Date Created:02/04/20
#  Date Last Modified:02/04/20

def Handicap():
    
    #Get the users dara
    a = int(input("Enter Game 1: "))
    b = int(input("Enter Game 2: "))
    c = int(input("Enter Game 3: "))

    #Calculating the average

    avg = int((a+b+c)/3)

    handicap = int((200-avg)*0.8)
    #Formatting output

    print("\nThe bowler's average is: ", avg)
    print("The bowler's handicap is: ", handicap)

Handicap()

    
