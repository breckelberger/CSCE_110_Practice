#File: q3.py
#Author: Breck Echelberger
#Date: 9/25/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description:Write a Python program stored in a file q3.py that:
#• Gets single-digit numbers from the user on one line (digits are separated by one white
#space) and adds them to a list. The first digit and last digit should not be a zero. If the
#user provides an invalid entry, the program should prompt for a new value. (5 points)
#• Converts every entry in the list to an integer and prints the list. The digits in the list repre-
#sent a non-negative integer. For example, if the list is [4, 5, 9, 1], the entries represent the
#integer 4591. The most significant digit is at the zeroth index of the list. Print the list and
#the reverse of the list. (5 points)
#• Find the absolute difference between the original list and the reversed list. For example:
#3if the list is [4, 5, 9, 1], the reverse of the list is [1, 9, 5, 4], and the resulting list from
#subtraction will be: [2, 6, 3, 7] from the logic abs(4591-1954) = 2637.

while True:
    nums = input("Enter the numbers: ").split()
    
    numlist = []
    
    for i in nums:
        numlist.append(int(i))

    if numlist[0] != 0 and numlist[-1] != 0:
        valid = True
        for i in numlist:
            if i < 0 or i >= 10:
                valid = False
        if valid:
            break
    print("Invalid entry. First and last digits must be non-zero, and all inputs should be single digits.")


print("The list is:", numlist)


reversenumlist = numlist[::-1]
print("The reverse of your list is:", reversenumlist)

initialnumber = 0
for i in numlist:
    initialnumber = initialnumber * 10 + i

secondnumber = 0
for i in reversenumlist:
    secondnumber = secondnumber * 10 + i

difference = initialnumber - secondnumber

print("The difference is:", difference)
