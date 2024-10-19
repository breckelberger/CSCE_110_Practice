#File: q3.py
# #Author: Breck Echelberger
#Date: 9/18/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a Python program (called q3.py) that asks the user to input the scores for 
# 5 subjects in a
#single line and stores them as numbers in an array.
#• Prints the average score of the student.
#• Prints the grade based on the criteria:
#– Score >= 90 : A
#– 90 > Score >= 80 : B
#– 80 > Score >= 70 : C
#– 70 > Score : D
#• The students can retake exam 5. Change score 5 such that the average score of the
#student becomes 95.
#• Print the updated array
#• Scores can integers between [0-100]. Print True if all scores in the array are valid, other-
#wise False.

scores = input("Enter five test scores: ").split()
scores = [int(i) for i in scores]

total = sum(scores)
avg = total / 5

print("The average score is: ", avg)

if avg >= 90:
    print("A")
elif 90 > avg >= 80:
    print("B")
elif 80> avg >= 70:
    print("C")
else:
    print("D")

fifthfor95 = (475) - (total - scores[4])
scores[4] = fifthfor95

print("Here is the updated scores", scores)

valid_scores = all(0 <= score <= 100 for score in scores)
print("Are all of the test scores valid?", valid_scores)