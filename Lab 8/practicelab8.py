class Conversion:
    def roman_to_int(self, s):
        '''
        roman_to_int method. Here, the input string s is converted to integer and the converted number is returned.
        '''
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        calc = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                calc -= roman[s[i]]
            else:
                calc += roman[s[i]]

        return calc
    
    def int_to_roman(self, num):
        '''
        int_to_roman method. Here, the input integer num is converted to roman and the converted number is returned.
        '''
        pass  # Placeholder for future implementation


print("To convert from Roman to Integer, enter 1.\nTo convert from Integer to Roman, enter 2.\nTo quit, enter 3.")
choice = input()
while choice != '3':

    if choice == '1':
        s = input("Enter roman numerals: ")
        
        # Create an instance of the Conversion class
        converter = Conversion()
        
        # Call the method using the instance of the class
        result = converter.roman_to_int(s)  # Correct way to call an instance method
        print(f"The integer value of {s} is {result}")

    elif choice == '2':
        s = input("Enter an integer: ")
        
        # Create an instance of the Conversion class
        converter = Conversion()
        
        # Call the method using the instance of the class
        result = converter.int_to_roman(int(s))  # Assuming you're passing an integer
        print(f"The Roman numeral of {s} is {result}")

    # Ask for the next choice
    choice = input("To convert from Roman to Integer, enter 1.\nTo convert from Integer to Roman, enter 2.\nTo quit, enter 3.")
