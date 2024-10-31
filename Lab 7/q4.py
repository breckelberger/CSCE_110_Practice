#File: q4.py
#Author: Breck Echelberger
#Date: 10/30/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description:Write a python program q4.py that contains a recursive function that prints the n-th row of Pas-
#cal’s Triangle. Pascal’s Triangle is given by: 
#The function should take the row number as the input and return the elements of that row in the
#form of a list. Make sure the sequence of elements should not be changed. No need for validity
#checking

def pascal(a):
    final = []

    if a == 0:
        return final
    elif a == 1:
        final.append(1)
        return final
    else:
        last = pascal(a - 1)
        final.append(1)

        for i in range(len(last) - 1):
            final.append(last[i] + last[i + 1])

        final.append(1)
        return final
    

a = int(input("Enter a row number for pascals triangle: "))
print(pascal(a))