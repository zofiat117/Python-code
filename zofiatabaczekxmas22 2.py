#user enters first name 
firstname = input("What is your first name? ")
#user enters surname
surname = input("What is your surname? ")
#says hello to user
print("Hello ",firstname, surname)
print("Please select from a list of items.\n")
print("\tItems Available")
print("1=Book\n2=Ruler\n3=Pen")
shoppingItem = int(input("\nEnter the number of item you would like: "))

if shoppingItem==1:
  print("You bought a book")
  
if shoppingItem==2:
  print("You bought a ruler")
  
if shoppingItem==3:
  print("You bought a pen")
  
if shoppingItem>3:
  print("Invalid choice. Goodbye!")
  
if shoppingItem<1:
  print("Invalid choice. Goodbye!") 