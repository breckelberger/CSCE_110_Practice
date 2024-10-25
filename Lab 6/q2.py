#File: q2.py
#Author: Breck Echelberger
#Date: 10/22/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: A pattern in a DNA sequence is defined using A, T, G, and, C repeatedly. Scientists often need
#to find the most recurring pattern of a specific length in the DNA sequence. Write a Python
#program stored in a file q2.py that takes a DNA sequence and the pattern length as inputs. The
#program should then print the least frequent pattern(s) of the requested length. Use a Python
#dictionary to store the patterns and their count and print them as shown in the example. There
#are some conditions for this problem:
#• You can not use any built-in function to sort a dictionary anywhere in the code. Using any
#built-in sorting function will cause a 20-point deduction.
#• you need to validate the input pattern length using an isValid() function. Not using this
#function will cause a 10-point deduction.
#• you need to loop until the user inputs valid input. It is not shown in the example. But, if
#your code does not have this functionality, there will be a 10-point deduction.
#• The pattern length should be greater than or equal to 2, integer, and less than the length
#of the input DNA sequence

def isValid(length, sequence):

    if isinstance(length, int) and length >= 2 and length < len(sequence):
        return True
    return False

def dnacalc():
    while True:

        userseq = input("Enter a DNA sequence: ").upper()

        valid_dna = True
        for i in userseq:
            if i not in ['A', 'T', 'C', 'G']: 
                print("The input entered is not correct. Only A, T, C, and G are allowed. Try again.")
                valid_dna = False
                break  
        
        if valid_dna:
            while True:
                try:
                    userlen = int(input("Enter the pattern length: "))
                    
                    if isValid(userlen, userseq):

                        main = {}

                        for i in range(len(userseq) - userlen + 1):
                            pattern = userseq[i:i + userlen]
                            if pattern in main:
                                main[pattern] += 1
                            else:
                                main[pattern] = 1

                        smallest = []
                        min_count = float('inf')
                        
                        for pattern, count in main.items():
                            if count < min_count:
                                min_count = count
                                smallest = [pattern]
                            elif count == min_count:
                                smallest.append(pattern)

                        print(f"""The patterns equal to the given pattern length present in the 
                              DNA sequence and the frequency patterns are: {main}""")
                        print(f"Least frequent pattern of length {userlen} is:")
                        for pattern in smallest:
                            print(pattern)

                    else:
                        print("The pattern length is not correct.")
                
                except ValueError:
                    print("Please enter a valid integer for the pattern length.")
            
            break

dnacalc()