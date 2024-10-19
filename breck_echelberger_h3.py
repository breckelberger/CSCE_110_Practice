#File: h3.txt
#Author: Breck Echelberger
#Date: 10/16/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a function, remove_string(s, n), which removes characters from string s from 0 up to n - 1 and returns a new string. 
#Note n is a positive integer. (5 pts)
#Ex1) remove_string(‘abcdefg’, 3) returns  ‘defg’.
#Ex2) remove_string(‘abcdefg’, 10) prints ‘too long’.
#Ex3) remove_string(‘abcdefg’, 7) prints ‘empty string’.
#Ex4) remove_string(‘abcdefg’) returns ‘abcdefg’.

def remove_string(s, n):

    if n < 0:
        print("Invalid Integer")
        exit()
    elif n > len(s):
        return "too long"
    elif n == len(s):
        return "empty string"
    else:
        y = s[n:]
        return y


s = input("Enter a word: ")
n = int(input("Enter a positive number: "))

print(remove_string(s, n))