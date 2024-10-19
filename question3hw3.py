#A list is sorted in ascending order if it is empty or each item except the last one is less than or equal to 
# its successor. Write a function isSorted() that expects a list as an argument and returns True if the list is 
# sorted in ascending order, or returns False otherwise. (5 pts)
#Ex1) isSorted([]) returns True.#
#
#Ex2) isSorted([10]) returns True.
#
#Ex3) isSorted([3, 9]) returns True.
#
#Ex4) isSorted([9, 3]) returns False.

def isSorted(a):
    if a == 0 or a == 1:
        return True
    
    for i in range(len(a) - 1):
        if a[i + 1] >= a[i]:
            return True
    return False

a = list(map(int, input("Enter integers separated by spaces: ").split()))

print(isSorted(a))