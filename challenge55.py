import random
num = random.randint(1, 5)
user = int(input("Pick a number between number 1 and 5: "))
if user == num :
    print("Well done")
else :
    if user > num :
        user = int(input("Too high, try again: "))
        if user == num :
            print("Correct")
        else :
            print("You lose")
    elif user < num :
        user = int(input("Too low, try again: "))
        if user == num :
            print("Correct")
        else :
            print("You lose")
        