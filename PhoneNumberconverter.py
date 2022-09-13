#Name: Phone Number Converter
#Author: Owen Maguire
#Date: 9/9/22
#Desc: Converts phone numbers with letters to normal phone numbers
#Location: Beaverton High School, Oregon

def LtrSorter():
  if i == "A" or i == "B" or i == "C":
    print("2")
  elif i == "D" or i == "E" or i == "F":
    print("3")
  elif i == "G" or i == "H" or i == "I":
    print("4")
  elif i == "J" or i == "K" or i == "L":
    print("5")
  elif i == "M" or i == "N" or i == "O":
    print("6")
  elif i == "P" or i == "Q" or i == "R" or i == "S":
    print("7")
  elif i == "T" or i == "U" or i == "V":
    print("8")
  elif i == "W" or i == "X" or i == "Y" or i == "Z":
    print("9")
  else:
    print(i)
    
  return "".replace("\r\n", "")      #remember to ask for help with spacing
  return "".strip("\r", "\n")




while True:

#User input
  print("This program will turn a phone number with letters into a normal phone number. \n")
  ognum = input("Please enter the phone number: ").upper()
  print()
  
#Formatting
  print("The phone number is: ", end = "")
  
#Converts letters into numbers and keeps the numbers the same
  for i in ognum:
    if i == "A" or i == "B" or i == "C":
      print("2", end = "")
    elif i == "D" or i == "E" or i == "F":
      print("3", end = "")
    elif i == "G" or i == "H" or i == "I":
      print("4", end = "")
    elif i == "J" or i == "K" or i == "L":
      print("5", end = "")
    elif i == "M" or i == "N" or i == "O":
      print("6", end = "")
    elif i == "P" or i == "Q" or i == "R" or i == "S":
      print("7", end = "")
    elif i == "T" or i == "U" or i == "V":
      print("8", end  = "")
    elif i == "W" or i == "X" or i == "Y" or i == "Z":
      print("9", end  = "")
    else:
      print(i, end = "")

  print("\n")

  
#Repeat program
  again = input("Run again? (Y/N)")
  if again[0].upper() == "N":
    break 