#File: q2.py
#Author: Breck Echelberger
#Date: 11/5/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: In this problem, you have to fill up the attached Python program called 
# q2.py in the appropriate places to build a conversion object that prompts the user to input a choice from a menu, 
# and based on the choice, makes appropriate conversions from Roman to Integer and Integer to Roman. 
# We are assuming that the user will only input Roman numbers and Integer numbers, so no need for validation. 
# Please try to recreate the example as shown in the pdf file named: “Example for Problem 2.pdf". 
# Please consult the Figure 1 for appropriate conversion. 
# Caution: the example pdf does not contain printing all the attribute and method names of the object. 
# But, you have to print that.
# Don’t make any changes to the given code except for places where you need to add your own code.

class Conversion:
    def roman_to_int(self, s):
        '''
        roman_to_int method. Here, the input string s is converted to integer and the converted number is returned.
        '''

        ####################################################
        
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        calc = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                calc -= roman[s[i]]
            else:
                calc += roman[s[i]]

        return calc
        

        ####################################################

    def int_to_roman(self, num):

        num = int(num)

        roman_tot = ''

        if num >= 1000:
            roman_tot += 'M' * (num // 1000)
            num %= 1000
        if num >= 900:
            roman_tot += 'CM'
            num -= 900
        if num >= 500:
            roman_tot += 'D'
            num -= 500
        if num >= 400:
            roman_tot += 'CD'
            num -= 400
        if num >= 100:
            roman_tot += 'C' * (num // 100)
            num %= 100
        if num >= 90:
            roman_tot += 'XC'
            num -= 90
        if num >= 50:
            roman_tot += 'L'
            num -= 50
        if num >= 40:
            roman_tot += 'XL'
            num -= 40
        if num >= 10:
            roman_tot += 'X' * (num // 10)
            num %= 10
        if num >= 9:
            roman_tot += 'IX'
            num -= 9
        if num >= 5:
            roman_tot += 'V'
            num -= 5
        if num >= 4:
            roman_tot += 'IV'
            num -= 4
        if num >= 1:
            roman_tot += 'I' * num
            num = 0
        
        return roman_tot

        ####################################################

print("To convert from Roman to Integer, enter 1.\nTo convert from Integer to Roman, enter 2.\nTo quit, enter 3.")
choice = input()
while choice != '3':

    ####################################################

    if choice == '1':
        s = input("Enter roman numerals: ")
        instance = Conversion()

        final = instance.roman_to_int(s)
        print(f'Converted number: {final}')

    else:
        num = input("Enter an integer: ")
        instance = Conversion()

        final = instance.int_to_roman(num)
        print(f'Converted numeral: {final}')



    choice = input("To convert from Roman to Integer, enter 1.\nTo convert from Integer to Roman, enter 2.\nTo quit, enter 3.")

####################################################
print("No attributes used but the methods roman_to_int and int_to_roman were used.")

####################################################