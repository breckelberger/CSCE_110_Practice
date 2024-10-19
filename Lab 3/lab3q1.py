#File: q1.py
# #Author: Breck Echelberger
#Date: 9/18/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a Python program (called q1.py) that asks the user to enter a number as input. The
#program then prints the reverse of the number and checks if the number is a palindrome or not.
#Note: You are not supposed to use in-build functions for finding the reverse. Use loops instead.
#You are supposed to take the input as an integer and it should not be converted to a list or a
#string at any point in your code

initial = int(input("Enter a whole number and I will evalute if it is palindrome: "))

ref_initial = initial 

reverse = 0

while 0 < initial:
    last_digit = initial % 10
    reverse = (reverse * 10) + last_digit
    initial = initial // 10
print("The reverse of your number is: ", reverse)

if reverse == ref_initial:
    print("Yes, this is a palindrome.")
else:
    print("No, this is not a palindrome.")