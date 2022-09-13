#Name: Fraction Reducer
#Author: Owen Maguire
#Date:9/13/22
#Desc: Simplifies the fraction to its simplest state. 
#Location: Beaverton high School, Oregon

#math module
import math

while True:
  #fraction input
  fraction = input("Please enter a fraction (x/y): ")
  if fraction == "0":
    break
  print()
  
  #turns fraction into two halves
  numbers = fraction.split("/")
  half1 = int(numbers[0])
  half2 = int(numbers[1])
  
  gcf = math.gcd(half1,half2)
  
  
  if gcf == 1:
    print(half1,"/",half2," Is the simplest form. ", sep = "")
  elif gcf != 1:
    numerator1 = half1 // gcf
    denominator1 = half2 // gcf
    
    numerator = round(numerator1, 0)
    denominator = round(denominator1, 0)
    
    print(numerator, "/", denominator, " Is the simplest form of ",half1, "/", half2, sep = "")