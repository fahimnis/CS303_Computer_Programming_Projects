#  File: Reverse.py
#  Description: Homework_4
#  Student's Name: Fahim N Islam
#  Student's UT EID: fni66
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: 2/6/20
#  Date Last Modified: 2/10/20

def Reverse():

    x = int(input("Enter an integer: "))

    a = int(x/100)

    b = int(x- a*100)

    c = int(a/10)

    d = int(b/10)

    e = a - c*10

    f = b - d*10

    g = f*1000 + d*100 + e*10 + c

    print("The reversed number is",g,end=".")

Reverse()
