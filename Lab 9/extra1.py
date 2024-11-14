#File: extra1.py
#Author: Breck Echelberger
#Date: 11/12/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a Python program stored in a file extra1.py which will ask the user to enter a number
#and returns the English word format of that number. The upper limit for this problem would be
#999,999. Make sure the output is properly formatted.

def numbertoenglish():
    initial = input("Enter a number: ")

    single_digit_numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
                            '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    double_digit_numbers = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
                            '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen',
                            '18': 'eighteen', '19': 'nineteen', '20': 'twenty'}
    tens_numbers = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
                    '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
    hundreds_number = {'1': 'one hundred', '2': 'two hundred', '3': 'three hundred',
                       '4': 'four hundred', '5': 'five hundred', '6': 'six hundred',
                       '7': 'seven hundred', '8': 'eight hundred', '9': 'nine hundred'}

    comparison_initial = int(initial)
    

    if 0 <= comparison_initial < 10:
        print(single_digit_numbers[initial])
    elif 10 <= comparison_initial < 20:
        print(double_digit_numbers[initial])
    
    elif 20 <= comparison_initial < 100:
        tens, ones = initial[0], initial[1]
        if ones == '0':
            print(tens_numbers[tens])
        else:
            print(tens_numbers[tens] + ' ' + single_digit_numbers[ones])
    
    elif 100 <= comparison_initial < 1000:
        hundreds, tens, ones = initial[0], initial[1], initial[2]
        if tens == '0' and ones == '0':
            print(hundreds_number[hundreds])
        elif tens == '0':
            print(hundreds_number[hundreds] + " and " + single_digit_numbers[ones])
        elif ones == '0':
            print(hundreds_number[hundreds] + " and " + tens_numbers[tens])
        else:
            print(hundreds_number[hundreds] + " and " + tens_numbers[tens] + ' ' + single_digit_numbers[ones])
    
    elif 1000 <= comparison_initial < 10000:
        thousands, hundreds, tens, ones = initial[0], initial[1], initial[2], initial[3]
        if hundreds == '0' and tens == '0' and ones == '0':
            print(single_digit_numbers[thousands] + ' thousand')
        elif tens == '0' and ones == '0':
            print(single_digit_numbers[thousands] + ' thousand ' + hundreds_number[hundreds])
        elif ones == '0':
            print(single_digit_numbers[thousands] + ' thousand ' + hundreds_number[hundreds] + " and " + tens_numbers[tens])
        else:
            print(single_digit_numbers[thousands] + ' thousand ' + hundreds_number[hundreds] + " and " + tens_numbers[tens] + ' ' + single_digit_numbers[ones])
    
    elif 10000 <= comparison_initial < 100000:
        ten_thousands, thousands, hundreds, tens, ones = initial[0], initial[1], initial[2], initial[3], initial[4]
        if hundreds == '0' and tens == '0' and ones == '0':
            print(single_digit_numbers[ten_thousands] + ' thousand')
        elif tens == '0' and ones == '0':
            print(single_digit_numbers[ten_thousands] + ' thousand ' + hundreds_number[hundreds])
        elif ones == '0':
            print(single_digit_numbers[ten_thousands] + ' thousand ' + hundreds_number[hundreds] + " and " + tens_numbers[tens])
        else:
            print(single_digit_numbers[ten_thousands] + ' thousand ' + hundreds_number[hundreds] + " and " + tens_numbers[tens] + ' ' + single_digit_numbers[ones])

    elif 100000 <= comparison_initial < 1000000:
        hundred_thousands, ten_thousands, thousands, hundreds, tens, ones = initial[0], initial[1], initial[2], initial[3], initial[4], initial[5]
        if tens == '0' and ones == '0':
            print(single_digit_numbers[hundred_thousands] + ' hundred thousand')
        elif ones == '0':
            print(single_digit_numbers[hundred_thousands] + ' hundred thousand and ' + tens_numbers[tens])
        else:
            print(single_digit_numbers[hundred_thousands] + ' hundred thousand and ' + tens_numbers[tens] + ' ' + single_digit_numbers[ones])

numbertoenglish()    