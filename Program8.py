#********************************************************************
#
#  Developer:         Renee White
#
#  Program #:         Program 8
#
#  File Name:         Program8.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          10-25-19
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter # 5
#
#  Description:
#     This program finds the roots of a quadratic
#     equation using the Quadratic Formula.
#
#********************************************************************

import math
import Disc

def main():
    developerInfo()
    try:
        print('Quadratic Formula and Root Solutions Program')
        print('')
        print('Enter an numerical value for A,B, and C')
        print('or enter a zero for A to exit program.')
        print('')
        coeffA = int(input('Enter the coefficient A: '))
        while coeffA != 0:
            coeffB = int(input('Enter the coefficient B: '))
            coeffC = int(input('Enter the coefficient C: '))
            disc = Disc.discriminant(coeffA, coeffB, coeffC)
            SqrRoot = math.sqrt(disc)
            X1 = (-coeffB+SqrRoot)/(2*coeffA)
            X2 = (-coeffB-SqrRoot)/(2*coeffA)
            print('\nDiscriminant is: ', disc)
            if disc == 0:
                print('The equation has one real solution.')
                print('X1 = ', X1)
                print('X2 = ', X2)
            else:
                print('The equation has two real solutions.')
                print('X1 = ', X1)
                print('X2 = ', X2)
            print('')
            print('Enter another numerical value for A,B, and C')
            print('or enter a zero for A to exit program.')
            print('')
            coeffA = int(input('Enter the coefficient A: '))
    except ValueError:
        print('The equation has two complex solutions.')
        print('but no real solutions.')
        
   # End of the main function 
        
def developerInfo():
    print('Name:     Renee White')
    print('Course:   Programming Fundamentals I')
    print('Program:  8')
    print()
    
    # End of the developerInfo function


    
# Call the main function
main()

# End of Program 8
