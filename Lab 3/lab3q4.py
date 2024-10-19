#File: q4.py
# #Author: Breck Echelberger
#Date: 9/18/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a python program (q4.py) that asks the user to enter the weights of 5 industry equipment
#in a single line. The program then performs the following tasks:
# Prints the mean of the 5 equipment.
# Prints the Variance of the sample.
# Print the Standard Deviation of the sample.
#Note: Use loops. You are not supposed to used math libraries or in-built functions

weights = input("Enter the weights of 5 industry equpiments: ").split()
weights = [int(i) for i in weights]

total = sum(weights)
avg = total / 5

varsum = 0

for i in weights:
    varsum += (i - avg) ** 2

var = varsum / 4

stad = var ** (1/2)

print("The mean of the weights is ", avg)
print("The variance of the weights is ", var)
print("The standard deviation of the weights is ", stad)