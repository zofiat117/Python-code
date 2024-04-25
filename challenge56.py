import random
num = random.randint(1,10)
user = int(input("Guess the number between 1 and 10: "))

while user != num :
    user = int(input("Try again: "))
    
    if user == num :
        print("Correct")