#File: q1.py
#Author: Breck Echelberger
#Date: 10/30/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a Python program (called q1.py) that contains a recursive function that finds the factorial
#of a given number. Note: The factorial of a number is given by N! = 1 * 2 * 3 * 4 * ... N, where
#N is a non-negative number. No need for validity checking.

def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a - 1)
    

a = int(input("Enter a number to calculate the factorial: "))
print(factorial(a))