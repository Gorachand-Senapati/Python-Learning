
import random

def guess():
    lucky = random.randint(1,50)
  
    while True:
        userInput = int(input("Enter your guess number between 1 to 50: "))
        if(lucky == userInput):
            print("you are lucky")
            break
        elif(userInput>lucky):
            print("low")
        else:
            print("high")

guess()