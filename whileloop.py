while True:
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter another number "))
    print("Inside while loop")
    choice= input("Do you want the loop to continue? Y/N ")
    if choice in ("Y", "y") :
        print("continuing")
    else:
        break