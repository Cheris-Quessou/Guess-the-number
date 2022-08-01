# Write your code here :-)
#This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

#Ask the player to take a guess
for guessesTaken in range(1, 7):
    print("Take a guess. ")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is to low. ")
    elif guess > secretNumber:
        print("Your guess is to high. ")
    else:
        break    #This condition is the correct guess!

if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number i was thinkig of was " + str(secretNumber))
