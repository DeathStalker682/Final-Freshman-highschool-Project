#Name: Text Statistics
#Author: Owen Maguire
#Date: 9/27/22
#Desc: Creates list of characters entered by the user
#Location: Beaverton High School, Oregon


#finding characters
def characters():
  text = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+{}[];:',.<>/?\|`~\""
  
  for ltr in range(len(text)):
      if text[ltr] in usertext:
        print(text[ltr], ":", sep = "", end = "")
      if text[ltr] in usertext:
        print((count[text[ltr]]))
  return ""

#-------------------------------------------------------

from collections import Counter

while True:
  print("Enter some text and this program will count how many characters of each type you used.", end = " ")
  
  #User input
  usertext = input().lower()
  while (len(usertext)) > 200:
    print("Please enter 200 or less characters", end = " ")
    text = input().lower()

  print("\n")
  
#counts characters in text
  count = Counter(usertext)
  
  
  print(characters())

#Repeat program
  again = input(" Graph Again? (Y/N)")
  if again[0].upper() == "N":
    break 