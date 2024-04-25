import random
num = random.randint(1,10)
user = int(input("Guess the number between 1 and 10: "))

while user != num :
    if user > num:
        user = int(input("Too high, try again: "))
    elif user < num:
        user = int(input("Too low, try again: "))
print("Correct!")