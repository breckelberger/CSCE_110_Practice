#File: q3.py
#Author: Breck Echelberger
#Date: 10/30/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a program q3.py that converts the decimal representation of a number into it’s binary
#equivalent and returns the answer as a string. The following steps are performed in order to
#convert a decimal to it’s binary equivalent.
#• Divide the number by 2.
#• The quotient is used a the input for the next recursive call.
#• The remainder becomes the current digit of the binary representation.
#• The steps are repeated until the quotient becomes 0.

def bincalc(a):
    if a == 0:
        return ''
    else:
        quotient = a // 2
        remainder = a % 2
        return bincalc(quotient) + str(remainder)

a = int(input("Enter a number to be converted into binary: "))
print(bincalc(a))