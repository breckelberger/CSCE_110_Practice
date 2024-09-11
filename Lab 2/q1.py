#File: q1.py
#Author: Breck Echelberger
#Date: 9/11/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a Python program (called q1.py) that asks the user for the length, width, and height of a
#box in feet (f t) as input and calculates the sum of all edges and volume of the box in meter (m).
#Print the output with 2 digits after the decimal point. You need to take input in the same line,
#where different values are separated by a space.r
#info: Sum of all edges = 4 × (length + width + height)
#Volume = length × width × height
#1 foot = 0.3048 m

user_input = input("Enter the length, width, and height of the box in feet: ").split()

length = float(user_input[0]) * .3048
width = float(user_input[1]) * .3048
height = float(user_input[2]) * .3048

sum_of_all_edges = round((4 * (length + width + height)), 2)
volume = round((length * width * height), 2)

print("The sum of all the edges is ", sum_of_all_edges, "meters.")
print("The volume is ", volume, "cubic meters.")