#Author: Owen Maguire 
#Name: Property Tax
#Date: 9/7/22
#Desc: A program that tells you the property tax of a property.
#Location: Beaverton High School, Oregon

while True:

#Prompt
  print("What is the value of your property? (Numbers only) ", end =" ")
  strVal = str(input())
  print()

#Determine if value is accepted
  while strVal.isdigit() == False:
    print("That is not a valid number, please try again. \n")
    print("What is the value of your property? (Numbers only) ", end =" ")
    strVal = str(input())
    
  
  intVal = int(float(strVal))
    
#Assessed Value
  AsdVal = intVal * 0.92
  
#Tax
  UnfTax = AsdVal / 100
  Tax = UnfTax * 1.05
  
  print("The value of your property is $", round(intVal, 2))
  print("The assessed value of your property is $", round(AsdVal, 2))
  print("The amount of property tax you pay will be $", round(Tax, 2))
  print()
  
#Repeat program
  again = input(" Calculate again? (Y/N)")
  if again[0].upper() == "N":
    break 