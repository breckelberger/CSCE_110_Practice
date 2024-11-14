#File: q1.py
#Author: Breck Echelberger
#Date: 11/5/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description:In this problem, you have to fill up the attached Python program called q1.py in the 
# appropriate places to build an employee object which prompts the user to input a choice from a menu, 
# and based on the choice, makes appropriate changes to the employee attribute defined in the class Employee. 
# Please try to recreate the example as shown in the pdf file named: “Example for Problem 1.pdf". 
# Caution: the example pdf does not contain printing all the attribute and method names of the object. 
# But, you have to print that.
# Don’t make any changes to the given code except for places where you need to add your own code.

class Employee():

    def __init__(self):
        '''
        Constructor Method. The instance attribute called employee is defined here.
        '''
        self.employee = {}

    def add(self, name, eid, title, dpt): #name: name of the employee, eid: Employee ID, title: Job title, dpt: Department
        '''
        Add method. New employee id is added to the employee attribute using this method.
        '''

        ####################################################
        
        self.employee[eid] = {'name': name, 'title': title, 'dpt': dpt}

        ####################################################
        

    def search(self, eid):
        '''
        Search method. Existing employee id is searched from the employee dictionary in this method.
        If the employe id is non existant, the program notifies user.
        '''
        
        ####################################################
        
        if eid in self.employee:
            return self.employee[eid]
        else:
            return "Employee id is non-existant in the dictionary."

        ####################################################
        
    def edit(self, eid):
        '''
        Edit method. Existing employee id is edited on the employee dictionary in this method.
        If the employe id is non existant, the program notifies user.
                '''
        
        ####################################################
        
        if eid in self.employee:
            name = input("Enter a new name or enter the same name as before: ")
            title = input("Enter a new title or enter the same title as before: ")
            department = input("Enter a new department or the same department as before: ")

            self.employee[eid] = {'name': name, 'title': title, 'department': department}
        else:
            return "Employee id is non-existant in the dictionary"

        ####################################################
        

    def delete(self, eid):
        '''
        Delete method. Existing employee id is deleted from the employee dictionary in this method.
        If the employe id is non existant, the program notifies user.
        '''
        
        ####################################################
        
        if eid in self.employee:
            del self.employee[eid]
        else:
            return "Employee id not found in the dictionary."

        ####################################################
    
    
company = Employee()
choice = input("Please input choice from the menu\n"+"*"*10+"Main Menu"+"*"*10+"\n1. Add Employee\n2.Look up Employee\n3.Edit Employee\n4.Delete Employee\n5.Quit\n"+"*"*30+'\n')

while choice != '5':

    ####################################################
    
    if choice == '1':
        name = input("Enter employee name: ")
        eid = input("Enter employee ID: ")
        title = input("Enter job title: ")
        dpt = input("Enter department: ")
        company.add(name, eid, title, dpt)

    elif choice == '2':
        eid = input("Enter employee ID to search: ")
        result = company.search(eid)
        print(result)

    elif choice == '3':
        eid = input("Enter employee ID to edit: ")
        result = company.edit(eid)
        print(result)


    elif choice == '4':
        eid = input("Enter employee ID to delete: ")
        result = company.delete(eid)
        print(result)

    ####################################################

       
    print("Employee in this company:\n",company.employee) #prints the instance attribute dictionary which contains all the employee information
    choice = input("\n\nPlease input choice from the menu\n"+"*"*10+"Main Menu"+"*"*10+"\n1. Add Employee\n2.Look up Employee\n3.Edit Employee\n4.Delete Employee\n5.Quit\n"+"*"*30+'\n')
    if choice == '5':
        print("You have decided to quit. Goodbye.")

####################################################

print("Attributes used:", company.employee)
print("Methods used: add, search, edit, delete")

####################################################