#File: q1.py
#Author: Breck Echelberger
#Date: 9/25/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: creates a list based on user input and then asks for a target. Finds two numbers in the list that multiply to equal the target number or else prints it can not.


while True:
    listlength = int(input("Enter the length of the list: "))

    if 3 <= listlength <= 12:
        break
    else:
        print("Not a valid response, try again.")

ind = 0
listone = []

for i in range(listlength):
    value = int(input(f"Enter the value at the {ind} index:"))
    if value > 0:
        listone.append(value)
        ind += 1
    else:
        print("The value must be greater then zero. Try again.")

target = int(input("Enter a target number: "))

for i in range(len(listone)):
    for j in range(i + 1, len(listone)):
        if listone[i] * listone[j] == target:
            print(f"Values {listone[i]} (index {i}) and {listone[j]} (index {j}) multiply to equal {target}.")
            break  
    else:
        continue
    break
else:
    print("No match was found.")