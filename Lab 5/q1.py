#File: q1.py
#Author: Breck Echelberger
#Date: 10/15/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a Python program stored in a file q1.py that has a function BuzzSaw() that takes a positive
#integer n as the input and performs the following operations for every number in range [1,n]:
#• If the number is divisible by 3, it prints BUZZ.
#• If the number is divisible by 5, it prints SAW.
#• If the number is divisible by both 3 and 5, it prints BUZZSAW.
#• It the number is not divisible by 3 or 5, it prints the number
#• Prints "INVALID INPUT" if the input is a floating point number or negative.

def Buzzsaw():
    initial = int(input("Enter a number: "))

    if initial < 1:
        print("INVALID INPUT")
    else:
        newinitial = int(initial)
        for i in range(1, newinitial + 1):
            if i % 3 == 0:
                if i % 5 == 0:
                    print("BUZZSAW")
                else:
                    print("BUZZ")
            elif i % 3 > 0 and i % 5 == 0:
                print("SAW")
            else:
                print(i)

Buzzsaw()