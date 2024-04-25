import random
hort = random.choice(["h","t"])
user = input("Heads or tails? (h/t): ")
if user == hort :
    print("Well done, the answer was", hort)
else :
    print("Bad luck")