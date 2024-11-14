#File: breck_echelberger_h5.txt
#Author: Breck Echelberger
#Date: 11/12/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Define a class Student with two attributes name and id. 
# Then add three methods to this class that compare two Student instances. 
# One method should test for equality. A second method should test for less than. 
# The third method should test for greater than or equal to. 
# In each case, the method returns the result of the comparison of the two students’ names.

class Student:
    
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def equality(self, selftwo):
        return self.name == selftwo.name

    def lessthan(self, selftwo):
        return self.name < selftwo.name      

    def greaterthan(self, selftwo):
        return self.name >= selftwo.name
    
one = Student('Breck', 0)
two = Student('Ridge', 1)

print(one.equality(two))
print(one.lessthan(two))
print(one.greaterthan(two))