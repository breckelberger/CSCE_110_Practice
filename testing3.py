characters = input("Enter a string: ")
length = len(characters)

first = characters[0]
last = characters[-1]
i =  length // 2
middle = characters[i]

total = first + middle + last

print(total)