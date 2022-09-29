#Name: Text Histogram
#Author: Owen Maguire
#Date: 9/19/22
#Desc: Creates histogram of characters entered by user
#Location: Beaverton High School, Oregon


#Finding Characters
def characters():
  print("LETTERS:")
  alpha = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+{}[];:',.<>/?\|`~\""
  
  for ltr in range(len(alpha)):
      if alpha[ltr] in text:
        print(alpha[ltr], ":", sep = "", end = "")
      if alpha[ltr] in text:
        for i in range(count[alpha[ltr]]):
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
  
  print(characters())

#Repeat program
  again = input(" Graph Again? (Y/N)")
  if again[0].upper() == "N":
    break 
    
#Ver. 1.1: Shortened the progrm to one funtion.
