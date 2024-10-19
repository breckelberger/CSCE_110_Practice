#File: q2.py
#Author: Breck Echelberger
#Date: 9/25/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Fibonacci Sequence are numbers in sequence, where each is the sum of the two previous
#numbers. The sequence starts from 0 and 1 and goes like 0, 1, 1, 2, 3, 5, 8, 13, ... etc.
#Write a Python program stored in a file q2.py that: asks for a starting and ending number
#in the same line (both will be integers). Then it prints all the Fibonacci numbers between them
#and including them with the length of the final Fibonacci sequence. If the starting and ending
#numbers are not included in the Fibonacci sequence, then: If the starting number is not in the Fibonacci sequence. Then find the number closest to
#it in the Fibonacci sequence and print from that number.
#f the starting number is not in the Fibonacci sequence and there are two numbers closest
#to it, then find both Fibonacci sequences including those numbers.
#If the ending number is not in the Fibonacci sequence, then find the number in the Fi-
#bonacci sequence which is smaller than the ending number, and print the Fibonacci se-
#quence till that number.

start = int(input("Enter a starting number: "))
end = int(input("Enter a end number"))

fibnums = []

a, b = 0, 1
while a <= end:
    fibnums.append(a)
    a, b = b, a + b
    
if start not in fibnums:
    newstart = fibnums[0]
    for i in fibnums:
        if i <= start:
            newstart = i
        else:
            break
    start = newstart

if end not in fibnums:
    newend = fibnums[-1]
    for j in fibnums:
        if j <= end:
            newend = j
        else:
            break
    end = newend

list = []
for k in fibnums:
    if start <= k <= end:
        list.append(k)

length = len(list)

print("The start number is", start, "and the end number is", end, ".")
print("The numbers inbetween the start and end are: ", list)
print("The length of the list is:", length)