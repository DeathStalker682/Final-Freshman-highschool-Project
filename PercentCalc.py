#Name: Percentage Calculator
#Author: Owen Maguire
#Date: 9/15/22
#Desc: determines percentages based on the inputted score and the total points score. 
#Location: Beaverton High School, Oregon

while True: 

#User inputs
  total = input("Please enter the total amount of points on the test: ")
  while total.isdigit() == False:
    print("Please enter only numbers")
    total = input("Please enter the total amount of points on the test: ")
  total = int(total)
    
  high = input("Please enter the highest score that was acheived: ")
  while high.isdigit() == False:
    print("Please enter only numbers")
    high = input("Please enter the highest score that was acheived: ")
  high = int(high)
  
  low = input("Please enter the lowest score that was acheived: ")
  while low.isdigit() == False:
    print("Please enter only numbers")
    low = input("Please enter the lowest score that was acheived: ")
  low = int(low)
  
  print("Out of", total, "points, the percentages are: ")
 
#Spacing
  print("================================================================================== ")

#Formatting into columns
  for i in range(high, high - 20, -1):
    for x in range(i ,low -1, -20):
#Outputting into numbers and percentages
      score = int(x)
      percentage = score / total * 100
      print(x,"=", round(percentage, 2), "%", end = " \t ")
    print()
  
  print("==================================================================================")

#Repeat program
  again = input(" Play again? (Y/N)")
  if again[0].upper() == "N":
    break