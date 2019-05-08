# Modified version of Guess My Number
# Challenge 3, chapter 3 python for the absolute beginner
# Player has limited number of guesses (5)
# If player exeeds limiteded amount
# Then a chastising message is displayed

import random

#Intro
print("Welcome to the new edition of 'Guess my Number'!")
print("You have 5 chances to guess the right number.")
print("Pick a number between 1 and 30.\n")

# Initial values
number = random.randint(1, 30)
tries= 1
guess = int(input("Guess the right number: "))

#Guessing loop
while guess != number:
    if tries >= 5:
        print("\nYou didn't get it, you loser!")
        break
    elif guess < number:
        print("higher! ")
    elif guess > number:
        print("lower! ")

    guess = int(input("Guess the right number: ")) 
    tries += 1

       
print("\nIt took you", tries, "tries!")
print("The correct number was:", number)

input("\n\nPress the enter key to exit.")

    
    
