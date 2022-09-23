#Name: Text Histogram
#Author: Owen Maguire
#Date: 9/19/22
#Desc: Creates histogram of characters entered by user
#Location: Beaverton High School, Oregon


#finding letters
def letters():
  print("LETTERS:")
  alpha = "abcdefghijklmnopqrstuvwxyz"
  
  for ltr in range(len(alpha)):
      if alpha[ltr] in text:
        print(alpha[ltr], ":", sep = "", end = "")
      if alpha[ltr] in text:
        for i in range(count[alpha[ltr]]):
          print("*", end = " ")
        print()
  return ""

  
#finding numbers
def number():
  print("NUMBERS:")
  numbers = "0123456789"
  
  for num in range(len(numbers)):
    if numbers[num] in text:
      print(numbers[num], ":", sep = "", end = "")
    if numbers[num] in text:  
      for i in range(count[numbers[num]]):
        print("*", end = " ")
      print()
  return ""


#finding special characters
def special():
  print("SPECIAL CHARACTERS:")
  other = "!@#$%^&*()-_=+{}[];:',.<>/?\|`~\""
  
  for char in range(len(other)):
    if other[char] in text:
      print(other[char], ":", sep = "", end = "")
    if other[char] in text:
      for i in range(count[other[char]]):
        print("*", end = " ")
      print()
  return ""

#-------------------------------------------------------

from collections import Counter

while True:
  print("Enter some text and this program will create a histogram showing how many characters of each type you used.", end = " ")
  
  #User input
  text = input().lower()
  while (len(text)) > 200:
    print("Please enter 200 or less characters", end = " ")
    text = input().lower()

  print("\n")
#counts characters in text
  count = Counter(text)
  
  
  print(letters())
  print(number())
  print(special())

#Repeat program
  again = input(" Graph Again? (Y/N)")
  if again[0].upper() == "N":
    break 