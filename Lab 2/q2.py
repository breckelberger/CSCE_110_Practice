#File: q2.py
#Author: Breck Echelberger
#Date: 9/11/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description:Suppose, you would like to apply for a bank loan of $15, 000. But, you are not sure about the
#interest rate and loan period. Therefore, you want to plan ahead and calculate the total payoff
#amount using the loan amount, loan period, and interest rate. Write a Python program stored in
#a file q2.py that asks the user for loan period (in years) and interest rate (in percentage) as user
#input and prints out the total payoff amount.
#Total payoff amount C can be calculated using the formula C = P (1 + r)n, where P is the
#loan amount in dollars), n is the loan period (in years), and r is the interest rate (0 ≤ r ≤ 1).
#Make sure your code checks for correct interest rate input

r_initial = input("Enter the interest rate(percentage): ")
n = int(input("Enter the loan period (in years): "))

r = float(r_initial) / 100

if r <= 1 or r >= 0:
    payoff_amount = round((15000 * (1 + r) ** n), 2)

    print("At", r, "interest rate, you need to pay", payoff_amount , "after", n, "years.")
else: 
    print("invalid interest rate")