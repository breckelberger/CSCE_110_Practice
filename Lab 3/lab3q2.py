#File: q2.py
# #Author: Breck Echelberger
#Date: 9/18/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a python program (called q2.py) that asks the user to enter a four digit year (YYYY) as an
#input and prints whether the year is a leap year or not.
#Rules for a year being leap year:
#• If divisible evenly by 4, a Gregorian year is a leap year, with a February 29 and 366 days
#(e.g. 1996/4 = 499, so 1996 is a leap year), UNLESS
#• If divisible evenly by 100, a Gregorian year is a normal year with 365 days (e.g.1900/100=19,
#so 1900 is a normal year of 365 days; as is 2100), UNLESS
#• If divisible evenly by 400, a Gregorian year is a leap year; so the year 2000 is a leap year.
#

initial_year = int(input("Enter a year and I will tell you if it's a leap year: "))

if 0 < initial_year:
    if initial_year % 400 == 0:
        print("This is a leap year.")
    elif initial_year % 100 == 0:
        print("This is not a leap year.")
    elif initial_year % 4 == 0:
        print("This is a leap year.")
    else:
        print("Not a leap year.")
else:
    print("Try again.")