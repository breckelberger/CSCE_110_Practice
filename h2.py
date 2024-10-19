#File: h2.txt
#Author: Breck Echelberger
#Date: 9/19/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Three problems

#problem 1:
sideone = int(input("Enter the length of side one: "))
sidetwo = int(input("Enter the length of side two: "))
sidethree = int(input("Enter the length of side three: "))

if sideone ** 2 == (sidetwo ** 2) + (sidethree ** 2):
    print("This is a right triangle.")
else:
    print("not a right triangle.")

#problem 2:
r = float(input("Enter the radius of a sphere: "))
d = r * 2
c = 2 * 3.141592 * r
s = 4 * 3.141592 * (r ** 2)
v = 4/3 * 3.141592 * (r ** 3)

print("The radius is ", r, ", diameter is ", d,", circumpherence is ", c, ", surface area is ", s,", and the volume is ", v)

#problem 3:

characters = input("Enter a string: ")
length = len(characters)

first = characters[0]
last = characters[-1]
i =  length // 2
middle = characters[i]

total = first + middle + last

print(total)