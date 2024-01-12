#ZofiaTabaczek
#Automated Shop Code
#15/11/2023

#user enters first name 
firstname = input("What is your first name? ")
#user enters surname
surname = input("What is your surname? ")
#says hello to user
print("Hello ",firstname, surname)
print("Please select from a list of items.\n")
#shows items available
print("\tItems Available")
print("1=Book\n2=Ruler\n3=Pen")
#asks user what item they would like
shoppingItem = int(input("\nEnter the number of item you would like: "))

#if one of the items on list chosen, buys
if shoppingItem==1:
  print("You bought a book")
  
if shoppingItem==2:
  print("You bought a ruler")
  
if shoppingItem==3:
  print("You bought a pen")
  
#if number not on list chosen, program says its invalid and ends
if shoppingItem>3:
  print("Invalid choice. Goodbye!")
  
if shoppingItem<1:
  print("Invalid choice. Goodbye!") 