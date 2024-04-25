#  LCCSSummer23-B 
# Name: Zofia
# This function multiplies two numbers 
def multiply(x, y):
    return x * y 
# This function divides two numbers
def divide(x, y):
    return x / y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

numcalc = int(input("Enter the number of calculations you wish to perform: "))

for i in range(numcalc) :
    print(f"\nCalculation {i+1}")

# Main Program
    import random # To generate random numbers
    print("Select operation.")
    print("1.Multiply")
    print("2.Divide")
    print("3.Add")
    print("4.Subtract")
# Take input from the user 
    choice = input("Enter choice(1/2/3/4): ")


    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    if int(choice) == 1:
        print(num1,"*",num2,"=", multiply(num1,num2))
    
    elif int(choice) == 2:
        divided = round(divide(num1,num2), 1)
        print(num1,"/",num2,"=", divided)

    elif int(choice) == 3 :
        print(f"{num1} + {num2} = {add(num1,num2)}")

    elif int(choice) == 4 :
        print(f"{num1} - {num2} = {subtract(num1,num2)}")
