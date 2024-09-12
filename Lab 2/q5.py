#File: q5.py
#Author: Breck Echelberger
#Date: 9/11/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description:Write a program stored in a file q5.py that asks the user to enter a sentence without any punc-
#tuation, symbols, or numbers. The program should then print the total number of letters in this
#sentence. Also, it will print the total number of occurrences of the first and last letter of the
#sentence.
#Hint: For your convenience, you might want to convert the input sentence into uppercase
#or lowercase

sentence = input("Enter a sentence without any punctuation, symbols, or numbers: ").lower()

total_letters = len(sentence)

first_letter = sentence[0]
last_letter = sentence[-1]


first_count  = sentence.count(first_letter)
last_count = sentence.count(last_letter)

total_count = first_count + last_count

print("This sentence has ", total_letters, "letters and the first letter is ", first_letter)
print("The last letter is ", last_letter, "and the total count of the first/last letter is ", total_count)