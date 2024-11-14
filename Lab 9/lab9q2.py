#File: q2.py
#Author: Breck Echelberger
#Date: 11/12/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a Python program stored in a file q2.py which will ask the user to enter a filename, and
#open the file for reading. Write a program that reads the file’s contents and determines the
#following:
#• The number of uppercase letters in the file
#• The number of lowercase letters in the file
#• The number of digits in the file
#• The number of whitespace characters in the file
#• The total occurrences of the word "and"/"And" in the file.
#A file in the appropriate format (named text.txt) can be downloaded from Canvas. The sam-
#ple output showing the behavior of the program is shown below.
#Note: A mismatch of ±2 in the counts is acceptable as long as your code is implemented
#correctly


file_name = input('Enter a file: ')

with open(file_name, 'r') as file:
    content = file.read()

    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'

    upper_count = 0
    lower_count = 0
    digit_count = 0
    whitespace_count = 0

    for i in content:
        if i in upper:
            upper_count += 1
        elif i in lower:
            lower_count += 1
        elif i.isdigit():
            digit_count += 1
        elif i.isspace():
            whitespace_count += 1

    and_And_count = content.lower().count('and')

print(f"upper case letters: {upper_count}, lower case letters: {lower_count}, total digits: {digit_count}, whitespace count: {whitespace_count}, and count: {and_And_count}")
    








