# Breck Echelberger
# UIN: 332003322
# Homework 1



# Question 1:
# Write a program that asks the user to input two integer numbers, then return their product.

first = int(input("Howdy! Enter the first number: "))
second = int(input("Enter the second number and I will return the product: "))

answer = first * second

print("The product of the two numbers you entered is: ", answer)

# Question 2:
# You can calculate the surface of a cube if you know the length of an edge. Write a program 
# that takes the length of an edge (an integer) as input and prints the cube’s surface area 
# as output.

edge = int(input("Enter the length of one edge of the square: "))

answer_two = 6 * edge * edge

print("The surface area of the cube is: ", answer_two)

#Question 3:
# Rewrite the following program after correcting all the errors. (25 pts)

print("Predictions are hard.")
print("Especially about the future.")
User_num = 5 * 10
print("User_num is: ", User_num)


#Question 4:
# Write a Python program that accepts an integer n (1 <= n <= 9) and 
# compute the value of n + nn + nnn. (25 pts)

#Example:
#Enter a number between 1 and 9: 5                                
#5+55+555=615.


initial = int(input("Enter a number to start: "))

if 1 <= initial <= 9:
    answer_three = (initial) + (initial * 11) + (initial * 111)

    print("The answer to this problem is: ", answer_three)

else:
     print("Number is not included in this set.")