#Name: Fraction Reducer
#Author: Owen Maguire
#Date:9/13/22
#Desc: Simplifies the fraction to its simplest state. 
#Location: Beaverton high School, Oregon

#math module
import math

while True:

  print()
  print("This program will simplify fractions. Type 0 to exit. \n")
  
#fraction input
  fraction = input("Please enter a fraction (x/y): ")
  if fraction == "0":
    break
  while fraction.find("/") < 0:
    fraction = input("Please enter a fraction (x/y): ")
    if fraction == "0":
      exit()
  print()
  
#turns fraction into two halves
  numbers = fraction.split("/")
  half1 = int(numbers[0])
  half2 = int(numbers[1])

#get greatest common factor
  gcf = math.gcd(half1,half2)
  
#if fraction is already in simplest form
  if gcf == 1:
    print(half1,"/",half2," Is the simplest form. ", sep = "")
#divides fractions by gcf to simplify
  elif gcf != 1:
    numerator1 = half1 // gcf
    denominator1 = half2 // gcf
    
    numerator = round(numerator1, 0)
    denominator = round(denominator1, 0)
    
    print(numerator, "/", denominator, " Is the simplest form of ",half1, "/", half2, sep = "")
    
#Repeat program
  again = input(" Play again? (Y/N)")
  if again[0].upper() == "N":
    break 
    
#Version 1.1: Made input fraction prompt repeat until a correect input was used. 
#Version 1.2: Made while true loop breakable.
