import random
score = 0

for _ in range(5):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    
    question = f"What is {num1} {operator} {num2}? "
    answer = int(input(question))
    
    if eval(f"{num1} {operator} {num2}") == answer:
        score += 1

print(f"You got {score} out of 5 questions correct.")