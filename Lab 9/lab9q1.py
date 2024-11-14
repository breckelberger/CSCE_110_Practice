#File: q1.py
#Author: Breck Echelberger
#Date: 11/12/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a Python program stored in a file q1.py which will ask the user to enter a filename, and
#open the file for reading. Write a program that reads the file’s contents and prints the total
#number of sentences in the file and calculates the average number of words per sentence. A
#file in the appropriate format (named sample.txt) can be downloaded from Canvas.

import re

def filesearch():

    file_name = input("Enter a filename: ")

    try:
        with open(file_name, 'r') as file:
            data = file.read()
            
            sentences = re.split(r'[.!?]', data)

            sentence_count = len(sentences)

            print(f"The total number of sentences is {sentence_count}.")

            total_word_count = 0
        
            for sentence in sentences:
                word_count = len(sentence.split())
                total_word_count += word_count

            word_avg = total_word_count / sentence_count

            print(f"The average number of words per a sentence is {word_avg}.")

    except:
        print("File not found.")


print(filesearch())