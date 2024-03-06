import pandas;
import random
# main.py
print("hello world")
def guessingGame():
    print("welecome to guessing game \n guess a number between 1 and 100 :" )
    attempts=10
    number= random.randint(1, 100)
    while(attempts>0):
        print(f"you have {attempts} left")
        x=input(" take a guess:")
        if(int(x)>number):
            print("too high!")
        elif(int(x)<number):
            print("too low!")
        else:
            print("You are correct!")
            break
        attempts-=1
    if(attempts==0):
        print(f"you lost! the correct answer was {number}")
guessingGame()
