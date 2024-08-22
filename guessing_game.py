import random

z = random.randint(1,10)
x = 3
i = 0
# y is the number a player guesses.
# x is the max number of attempts
# i is the counter.
# z is the randomly generated number the player must guess.

print("Let's play a game!")
print("I am going to pick a random number between 1 and 10.") 
print("You have three attempts to guess the correct number.")
ready = input( "Are you ready to play? (Yes/No)")

if ready in ['Yes']:
    print("Okay! I have picked a number.")

    while i < x:
        y = int(input("What is your guess?"))
        if y == z:
            print("That's correct!")
            break
        else:
            print("That's not right! Try again.")
            i += 1

    if i == x:
        print("You lose!")

else:
    print(":(")