#File: q2.py
#Author: Breck Echelberger
#Date: 10/30/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Ackermann’s Function is a recursive mathematical algorithm that can be used to test how well a
#system optimizes its performance of recursion. In a Python file q2.py, write a recursive method,
#ackermann(m,n) which solves Ackermann’s Function. Use the following logic in your function:
#f m = 0, return n+1
#• if n = 0, return ackermann(m-1,1)
#• otherwise, return ackermann(m-1, ackermann(m,n-1))
#No need for validity checking.

def ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

m = int(input("Enter a number: "))
n = int(input("Enter a second number: "))

print(ackermann(m, n))