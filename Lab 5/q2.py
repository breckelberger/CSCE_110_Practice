#File: q2.py
#Author: Breck Echelberger
#Date: 10/15/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a Python program stored in a file q2.py that takes two numbers <start, end> as input from
#the user in a single line and performs the following tasks:
#• Has a boolean function called isValid() which takes a number as input and returns true if
#it is a positive integer otherwise returns false. (9 points)
#• It contains a boolean function isPrime() the returns true if the input argument is prime
#otherwise false. The program prints if the two inputs are prime or not. (10 points)
#• Has a void function printPrimes(), which takes the start and end values and prints all the
#prime numbers in that range followed by the count of prime numbers in the range. It makes
#use of isPrime() function to check if the numbers are prime or not.

def isValid(start, end):
    return start > 0 and end > 0

def isPrime(c):
    for i in range(2, int(c**0.5) + 1):
        if c % i == 0:
            return False
    return True 

def printPrimes(start, end):
    p = [i for i in range(start, end + 1) if isPrime(i)]
    print(f"Which prime numbers are in between the two provided numbers? {p}")
    print(f"How many prime numbers total? {len(p)}")


a = input("Enter two numbers separated by a space: ")

b = a.split()

start, end = map(int, b)

if isValid(start, end):
    print(f"Is {start} prime? {isPrime(start)}")
    print(f"Is {end} prime? {isPrime(end)}")
    printPrimes(start, end)
else:
    print("Try Again")