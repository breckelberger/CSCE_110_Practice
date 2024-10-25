#File: q1.py
#Author: Breck Echelberger
#Date: 10/22/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a Python program stored in a file q1.py that creates a dictionary for a flower shop with
#flower names as keys and 3 flower prices as values. The user can enter one choice from a
#menu, and continue to do so in a loop until "Quit" is selected. This menu should be printed as
#shown in the example image. For different options in the menu:
#• option 1: add a new flower and prices. Follow the example to do that. (6 points)
#• option 2: edit a flower if it is present in the current dictionary. If not, print as so. (8 points)• 
# option 3: delete a flower key and all the price values if the flower is present in the cur-
#rent dictionary. If not, print as so. The user can also delete the entire stock by inputting
#"All"/"all"/"aLL" or other forms of the word all. (10 points)
#• option 4: search for a flower key in the dictionary (8 points)
#• option 5: Quit the loop (7 points + 1 point for header)
#Make sure that the names of the flowers are string, and the prices are a list of float numbers.
#t the end of each loop, print the updated stock dictionary. The example shows a single run of
#the code, where the while loop worked until the user inputs 5 at the end. Replicate the example
#and make sure that your code is foolproof, so, other inputs will also work (For example: if "All"
#is entered in choice 3, what happens is not shown in the example. You have to make sure that
#your code works for delete all). The example for this problem is divided between two images for
#lack of space.

flowers = {}
prices = []

def mainmenu():
    print("******************** Main Menu ********************"
          "\n 1. Add Flower \n 2. Edit Flower \n 3. Delete Flower \n 4. Search Flower \n 5. Quit \n"
          "***************************************************")
    
    while True:
        a = int(input("Enter menu choice: "))

        if a == 1:
            info = input("Enter flower followed by prices. Give a comma after the flower name and a space inbetween prices: ").split(',')

            name = info[0].strip()
            prices = info[1].strip().split()

            prices = [float(price) for price in prices]

            flowers[name] = prices

        elif a == 2:
            edit = input("Enter the flower name: ")
            new_prices = input("Enter the renewed prices, seperated by spaces: ").strip().split()

            new_prices = [float(price) for price in new_prices]

            flowers[edit] = new_prices

        elif a == 3:
            flowerdelete = input("If you want to remove all items, enter 'all', otherwise, enter the flower name: ").lower()
            if flowerdelete == 'all':
                flowers.clear()
            else:
                if flowerdelete in flowers:
                    del flowers[flowerdelete]
                else:
                    print(f"{flowerdelete} is not in the list.")

        elif a == 4:
            flowerfind = input("Enter the flower name to search: ")

            if flowerfind in flowers:
                print(f"Here is the information for {flowerfind}: {flowers[flowerfind]}")
            else:
                print(f"{flowerfind} is not in the list.")

        elif a == 5:
            print("Current stock: ", flowers)
            break

        else:
            print("Not a valid menu selection")
        
        print("Current stock: ", flowers)
  
mainmenu()