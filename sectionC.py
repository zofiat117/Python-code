num1 = int(input("Enter a number "))
num2 = int(input("Enter a second number "))
choice = input("A or S? ")
    
if choice == 'a' or choice == 'A':
    print (num1 + num2)
elif choice == 's' or choice == 'S':
    print (num1 - num2)
else :
    print ("Invalid character")
    
