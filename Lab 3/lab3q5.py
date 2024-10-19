#File: q5.py
# #Author: Breck Echelberger
#Date: 9/18/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a program stored in a file q5.py that asks the user to enter a string and performs the
#following tasks.
#• Checks if the string follows all the constrains given below otherwise it prints "Invalid String"
#and terminates:
# The length is equal to 6
# It starts with an Upper Case letter
# Every letter is followed by one number
# A letter cannot be followed by a letter
# A number cannot be followed by a number
# String ends with ’!’
# Extract only the letters from the string and store it in a variable and print the variable
# Extract only the numbers from the string and store it in a variable
# Store all the positive divisors of the number in an array and print the array.
# If the number is prime, print YES otherwise NO

test = input("Enter a string: ")

if len(test) == 6: 
    if 'A' <= test[0] <= 'Z':
        if test[-1] == '!':
            valid = True
            letters = ""
            numbers = ""
            for i in range(1, 5, 2):
                if '0' <= test[i] <= '9':
                    if 'a' <= test[i-1] <= 'z' or 'A' <= test[i-1] <= 'Z': 
                        letters += test[i-1]
                        numbers += test[i]  
                    else:
                        valid = False
                else:
                    valid = False
            if valid:
                print("Valid string")
                print("The letters are:", letters)
                print("The numbers are:", numbers)
                number = int(numbers)

                divisors = [i for i in range(1, number + 1) if number % i == 0]
                print("The divisors are:", divisors)

                if len(divisors) == 2:
                    print("YES")
                else:
                    print("NO")
            else:
                print("Invalid string")
        else:
            print("Invalid string")
    else:
        print("Invalid string")
else:
    print("Invalid string")