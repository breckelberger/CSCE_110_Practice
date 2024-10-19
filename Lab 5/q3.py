#File: q3.py
#Author: Breck Echelberger
#Date: 10/15/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: The permutation of two numbers n and k is given by nPk = n!
#(n−k)! Write a Python program stored
#in a file q3.py that takes two integers <n,k> as inputs in two separate lines and performs the
#following tasks:
#• Contains a boolean function isValid() which takes n and k as input arguments and returns
#true their value is valid otherwise returns false. The program prints an error message and
#terminates if the inputs are invalid. (9 points)
#• Has a function getFactorial() which returns the factorial of the input argument. The program
#prints the factorial of n and k. (15 points)
#• Has a function getPermutation() that takes n and k as the input and return the value of nPk

def isValid(n, k):
    if n >= 0 and k >= 0:
        if k <= n:
            return True
    print("Not valid entries")
    return False
       
def getFactorial(a):
    f = 1
    for i in range(2, a + 1):
        f *= i
    return f

def getPermutation(n, k):
    b = getFactorial(n)
    c = n - k
    d = getFactorial(c)
    p = b / d
    return p
        


n = int(input("Enter a number: "))
k = int(input("Enter a second number: "))

if not isValid(n, k):
    exit()

print(getFactorial(n))
print(getFactorial(k))
print(getPermutation(n, k))


