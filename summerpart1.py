#  LCCSSummer23-A 
# Name: 
 
name = input("Please enter your name: ")
print(f"Hello {name}.\nWelcome to the add or subtract calculator.")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

while True:
    choice = input('Do you want me to (a)dd or (s)ubtract?: ')
    choice = str.lower(choice)

    if choice == 'a':
        print(f"{num1} + {num2} = {num1 + num2}")
        break
    elif choice == 's':
        print(f"{num1} - {num2} = {num1 - num2}")
        break
    else:
        print("Invalid choice!")

    
