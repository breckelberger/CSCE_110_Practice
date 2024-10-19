#Write a function called f_list() that does the following operations. (5 pts)
#Ex1) When a = [1, 2, 3, 4], f_list(a, 1) returns the product of all the numbers in the list which is 24.#
#
#Ex2) f_list(a, 2) returns the summation of all the numbers in the list which is 10.#
#
#Ex3) If the second argument is omitted, a default value 1 is used. f_list(a) returns 24.
#
#Note) Do not include a = [1, 2, 3, 4] in your program.

def f_list(a, b = 1):
    if b == 1:
        c = 1
        for i in a:
            c *= i
        return c
    elif b == 2:
        return sum(a)
    else:
        return 'Try again and make sure to include a value for b.'
    

a = list(map(int, input("Enter integers separated by spaces: ").split()))

b = input("Enter a value for b: ")

if b == '':
    print(f_list(a))
else:
    b = int(b)
    print(f_list(a, b))