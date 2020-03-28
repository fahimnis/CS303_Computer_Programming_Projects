#  File: NextDay.py
#  Description: HW4
#  Student's Name:Fahim N Is
#  Student's UT EID: fni66
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: 2/11/20
#  Date Last Modified: 2/13/20

def NextDay():

#Take inputs
    y = int(input("Please enter the year: "))
    m = input("Please enter the month: ")
    d = int(input("Please enter the day: "))
    n = d + 1
    ny = y + 1
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

#check for leap year
    if (y%4 == 0 and y%100 != 0) or (y%400 ==0):

        if m == F:

            if d == 28:

                print("The next day is February 29,",y,end=".")

            elif d == 29:

                print("The next day is",M,end=" 1, ")
                print(y,end=".")

            else:
                 print("The next day is",m,end = " ")
                 print(n,end=", ")
                 print(y,end=".") 
             

    #Check for months with 31 days within leap years            
        elif d == 30:

            if (m == J or m == M or m == MA or m == JUL or m == AUG or
                m == O or m == D):
                
                print("The next day is",m,end = " 31, ")
                print(y,end=".")


#check for months with 31 days            
    elif d == 30:

        
        
        if (m == J or m == M or m == MA or m == JUL or m ==
          AUG or m == O or m == D):
            
            print("The next day is",m,end = " 31, ")
            print(y,end=".")
            
        elif m == A:
            print("The next day is",MA,end=" 1, ")
            print(y,end=".")

        elif m == JU:
            print("The next day is",JUL,end=" 1, ")
            print(y,end=".")

        elif m == S:
            print("The next day is",O,end=" 1, ")
            print(y,end=".")

        elif m == N:
            print("The next day is",D,end=" 1, ")
            print(y,end=".")

#switching to next month if last day
    elif m == J:
        if d == 31:
            print("The next day is",F,end=" 1, ")
            print(y,end=".")

        else:
            print("The next day is",m,end = " ")
            print(n,end=", ")
            print(y,end=".")

            
    elif m == F:
        if (y%4 == 0 and y%100 != 0) or (y%400 ==0):

            if d == 28:

                print("The next day is February 29,",y,end=".")
                
            elif d == 29:

                print("The next day is",M,end=" 1, ")
                print(y,end=".")

            else:

                print("The next day is",m,end=" ")
                print(n,end=",")
                print(y,end=".")
                
            
        elif d == 28:
            print("The next day is",M,end = " 1, ")
            print(y,end=".")

        else:

            print("The next day is",m,end=" ")
            print(n,end=",")
            print(y,end=".")

            
    elif m == M:
        if d == 31:
            print("The next day is",A,end=" 1, ")
            print(y,end=".")

        else:
            print("The next day is",m,end = " ")
            print(n,end=", ")
            print(y,end=".")



    elif m == A:
        if d == 30:
            print("The next day is",MA,end=" 1, ")
            print(y,end=".")

        else:
            print("The next day is",m,end = " ")
            print(n,end=", ")
            print(y,end=".")


    elif m == MA:
        if d == 31:
            print("The next day is",JU,end=" 1, ")
            print(y,end=".")

        else:
            print("The next day is",m,end = " ")
            print(n,end=", ")
            print(y,end=".")



    elif m == JU:
        if d == 30:
            print("The next day is",JUL,end=" 1, ")
            print(y,end=".")

        else:
            print("The next day is",m,end = " ")
            print(n,end=", ")
            print(y,end=".")



    elif m == JUL:
        if d == 31:
            print("The next day is",AUG,end=" 1, ")
            print(y,end=".")

        else:
            print("The next day is",m,end = " ")
            print(n,end=", ")
            print(y,end=".")



    elif m == AUG:
        if d == 31:
            print("The next day is",S,end=" 1, ")
            print(y,end=".")

        else:
            print("The next day is",m,end = " ")
            print(n,end=", ")
            print(y,end=".")



    elif m == S:
        if d == 30:
            print("The next day is",O,end=" 1, ")
            print(y,end=".")

        else:
            print("The next day is",m,end = " ")
            print(n,end=", ")
            print(y,end=".")



    elif m == O:
        if d == 31:
            print("The next day is",N,end=" 1, ")
            print(y,end=".")
        else:
            print("The next day is",m,end = " ")
            print(n,end=", ")
            print(y,end=".")



    elif m == N:
        if d == 30:
            print("The next day is",D,end=" 1, ")
            print(y,end=".")

        else:
            print("The next day is",m,end = " ")
            print(n,end=", ")
            print(y,end=".")



    elif m == D:
        if d == 31:
            print("The next day is",J,end=" 1, ")
            print(ny,end=".")

        else:
            print("The next day is",m,end = " ")
            print(n,end=", ")
            print(y,end=".")


NextDay()
