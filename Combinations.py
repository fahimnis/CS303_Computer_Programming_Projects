#  File: Combinations.py
#  Description: HW9
#  Student's Name: Fahim Noor Islam
#  Student's UT EID: fni66
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: 03/10/2020
#  Date Last Modified: 03/10/2020

def factorial(num):

    fact = 1

    for i in range(1,num+1):

        fact = fact*i

    return fact

def combination(n,r):

    return factorial(n)/(factorial(r)*factorial(n-r))


def main():

    print(""*23)

    print('{:11s}{:>12s}'.format('Cards','Combinations'))
    print("="*23)

    for i in range(0,53):

        com = combination(52,i)

        print ( '{:>3d}{:>19d}'.format(int(i),int(com)))



    print(""*23)
    


main()






