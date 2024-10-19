#You work at a pizza restaurant, which is starting to accept orders online. You need to provide a python function 
# that will accept an arbitrary order as its arguments and compute the correct price for the order.
#Your cost-calculator function should have four arguments:
#pizzas
#drinks
#wings
#coupon
#A single pizza order is formed as a list of toppings. For example
#
#A pizza with no toppings (other than cheese and sauce) is: [] (an empty list)
#A pizza with pepperoni and a double order of olives is: ["pepperoni", "olives", "olives"]
#An arbitrary number of pizzas may be ordered, including no pizzas at all. Drinks come in as a named order 
# (i.e. a keyword argument 'drinks'). If drinks are ordered, they are specified as a list of sizes 
# (possible sizes: "small", "medium", "large", "tub"). For example, drinks = ["small", "small", "large"] 
# would indicate an order including two small drinks and a large drink. 
# Wings come in as a named order as well (keyword argument 'wings'). If wings are ordered, 
# they are specified as a list of integers (possible sizes: 10, 20, 40, 100). For example, 
# wings = [20] would indicate a single order of 20-piece wings.
#
#A coupon may be specified as the keyword argument 'coupon'. It will be a single floating-point number between 0 and 1. 
# This indicates the fraction of the pre-tax price that is to be subtracted. 
# For example, coupon=.25 would indicate a 25%-off coupon. A 6.25% tax is applied to every order. 
# The tax is computed on the total cost of the order before a coupon is applied.
#Prices#
#Pizza
#$13.00

#Toppings
#pepperoni: $1.00
#mushroom: $0.50
#olive: $0.50
#anchovy: $2.00
#ham: $1.50

#Drinks#
#small: $2.00
#medium: $3.00
#l#arge: $3.50
#tub: $3.75

#Wings
#10: $5.00
#20: $9.00
#40: $17.50
#100: $48.00 

#You can assume that the front-end of the website will never pass your function erroneous orders. 
# That is, you will never receive orders for items that do not exist nor items that contain typos.
#
#Note 1: You have to use a dictionary for the prices above inside your cost_calculator() function. 
# (Do not call another function that returns prices. In your program, there has to be only one function and 
# 3 function calls. Built-in function calls are okay.)
#
#Note 2: You must use the following cost_calculator() function and 3 function calls in your program. 
# (If you change the code below, your score will be 0.)
#
#(85 pts)

def cost_calculator(*args, drinks = [], wings = [], coupon = 0):
    
    menu = {"Pizza": {"price": 13.00},
            "Toppings": {"pepperoni": 1.00, "mushroom": 0.50, "olive": 0.50, "anchovy": 2.00, "ham": 1.50,},
            "drinks": {"small": 2.00, "medium": 3.00, "large": 3.50, "tub": 3.75},
            "wings": {"10": 5.00, "20": 9.00, "40": 17.50, "100": 48.00},}

    total_cost = 0

    for pizza in args:
        total_cost += menu["Pizza"]["price"]
        for topping in pizza:
            if topping in menu["Toppings"]:
                total_cost += menu["Toppings"][topping]

    for drink in drinks:
        if drink in menu["drinks"]:
            total_cost += menu["drinks"][drink]

    for wing in wings:
        wing_str = str(wing)
        if wing_str in menu["wings"]:
            total_cost += menu["wings"][wing_str]

    tax = total_cost * .0625

    if coupon > 0:
        total_cost *= (1 - coupon)
    
    total_cost += tax

    return total_cost


# first function call. prints $35.61

print(f"${cost_calculator([], ['ham', 'anchovy'], drinks = ['tub', 'tub'], coupon = 0.1):.2f}")

# second function call. prints $2.12

print(f"${cost_calculator(drinks = ['small']):.2f}")

# third function call. prints $60.56

print(f"${cost_calculator([], [], ['pepperoni', 'pepperoni'], wings = [10, 20], drinks = ['small']):.2f}")