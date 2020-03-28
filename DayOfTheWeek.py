#  File: DayOfTheWeek.py
#  Description: HW6
#  Student's Name:Fahim N Islam
#  Student's UT EID: fni66
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: 2/20/20
#  Date Last Modified: 2/20/20

def DayOfTheWeek():

    year = int(input("Please enter the year (an integer): "))
    month = input("Please enter the month (a string): ")
    day = int(input("Please enter the day (an integer): "))

    #Setup some useful variables
    J = "January"
    F = "February"
    M = "March"
    A = "April"
    MA = "May"
    JU = "June"
    JUL = "July"
    AUG = "August"
    S = "September"
    O = "October"
    N = "November"
    D = "December"

    #setup lists to access the ordered pairs easily
    
    Zeller = [11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
    M = [J,F,M,A,MA,JU,JUL,AUG,S,O,N,D]

    #loop through the lists to set a if the month matches. please don't mark me off for using enumerate

    for i,j in enumerate(M):
        if month == j:
            a = Zeller[i]
            #print(a)

    b = day

    if month == J or month == F:
        year = year - 1
        d = year//100
        c = year%100
    else:
        d = year//100
        c = year%100

    w = (13 * a - 1 ) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    r = (r + 7) % 7

    Days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    Result = [0,1,2,3,4,5,6]

    for i,j in enumerate(Result):
        if r == j:
            DOTW = Days[i]

    print("The day of the week is ",DOTW,end=".")
    

DayOfTheWeek()
