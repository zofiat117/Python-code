import random

colors = ["red", "blue", "green", "yellow", "orange"]
answer = random.choice(colors)
user_color = input("Pick a color from the list (red, blue, green, yellow, orange): ")

while user_color != answer:
    if answer == "red":
        print("You must be seeing RED right now.")
    elif answer == "blue":
        print("You must be feeling pretty BLUE.")
    elif answer == "green":
        print("I bet you are GREEN with envy.")
    elif answer == "yellow":
        print("You're probably feeling YELLOW with caution.")
    elif answer == "orange":
        print("I hope you're not feeling too ORANGE.")
    
    user_color = input("Guess again: ")

print("Well done!")