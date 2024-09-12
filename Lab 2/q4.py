#File: q4.py
#Author: Breck Echelberger
#Date: 9/11/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a program stored in a file q4.py that asks the user for the cost of lunch for five working
#days and prints out the average cost and total cost with two digits after the decimal point. You
#need to take input in the same line, where different values are separated by a space.
#use a loop

costs_str = input("Enter lunch costs for five working days: ").split()

costs = []

for i in costs_str:
    costs.append(float(i))

average = round(sum(costs) / len(costs), 2)

total = round(sum(costs), 2)

print("The total cost of lunch this week is", total, ".")
print("On average you spend", average,"daily for lunch.")