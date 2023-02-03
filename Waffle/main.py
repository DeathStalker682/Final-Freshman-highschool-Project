# Name: Waffle
# Author: Owen Maguire
# Date: 1/31/23
# Desc: Create a 2D Rubiks cube model called a "Waffle"
# Location: Beaverton High School, Oregon

from class_file import Shuffle #imports class


r1 = Shuffle([0,0,0,0,0,0])
r2 = Shuffle([0,0,0,0,0,0])
r3 = Shuffle([0,0,0,0,0,0]) #creating grid with objects
r4 = Shuffle([0,0,0,0,0,0])
r5 = Shuffle([0,0,0,0,0,0])
r6 = Shuffle([0,0,0,0,0,0])

r1.shuffle()
r2.shuffle()
r3.shuffle() #method that shuffles 
r4.shuffle()
r5.shuffle()
r6.shuffle()

r1 = r1.line
r2 = r2.line
r3 = r3.line #turning method outputs into variables
r4 = r4.line
r5 = r5.line
r6 = r6.line


c1 = [r1[0],r2[0],r3[0],r4[0],r5[0],r6[0]]
c2 = [r1[1],r2[1],r3[1],r4[1],r5[1],r6[1]]
c3 = [r1[2],r2[2],r3[2],r4[2],r5[2],r6[2]] #columns
c4 = [r1[3],r2[3],r3[3],r4[3],r5[3],r6[3]] 
c5 = [r1[4],r2[4],r3[4],r4[4],r5[4],r6[4]]
c6 = [r1[5],r2[5],r3[5],r4[5],r5[5],r6[5]]


row1 = "r1" 
row2 = "r2" 
row3 = "r3" 
row4 = "r4" 
row5 = "r5" 
row6 = "r6" 

column1 = "c1"
column2 = "c2"
column3 = "c3"
column4 = "c4"
column5 = "c5"
column6 = "c6"

row_list = [row1, row2, row3, row4, row5, row6] #put row text into a list
column_list = [column1, column2, column3, column4, column5, column6] #column text into list

r = [r1, r2, r3, r4, r5, r6] #put rows into a list
c = [c1, c2, c3, c4, c5, c6] #put columns into list

column_number = {"c1":0, "c2":1, "c3":2, "c4":3, "c5":4, "c6":5}
row_number = {"r1":0, "r2":1, "r3":2, "r4":3, "r5":4, "r6":5}

solved = True
#####################################################
def shuffle_waffle():
  r1 = Shuffle([0,0,0,0,0,0])
  r2 = Shuffle([0,0,0,0,0,0])
  r3 = Shuffle([0,0,0,0,0,0]) #creating grid with objects
  r4 = Shuffle([0,0,0,0,0,0])
  r5 = Shuffle([0,0,0,0,0,0])
  r6 = Shuffle([0,0,0,0,0,0])
  
  r1.shuffle()
  r2.shuffle()
  r3.shuffle() #method that shuffles 
  r4.shuffle()
  r5.shuffle()
  r6.shuffle()
  
  r1 = r1.line
  r2 = r2.line
  r3 = r3.line #turning method outputs into variables
  r4 = r4.line
  r5 = r5.line
  r6 = r6.line

  return""
#####################################################
def output():
  
  #print out waffle
  for i in range(6):
    row = r[i]
    for i in range(6):
      if row[i] == 1:
        print(u'\u25a1', end = ' ') #white
      elif row[i] == 0:
        print(u'\u25a0', end = ' ') #black
    print()
  print("\n")
  return ""
  
#####################################################

def flip_row():

  x = ""
  while x not in row_number: #determine which row to flip
    x = row_input
  x = row_number[x]
  
  for i in range(6):
    if row_input != row_list[i]: #iterate through row list
      continue    #until it hits the right row
    row = r[i]
    for i in range(6): #change 1 to 0 or 0 to 1,  
      if row[i] == 1:  #"flips" the row
        row[i] = 0             
      elif row[i] == 0:
        row[i] = 1
      c[i][x] = row[i] #make  rows = to columns
  return ""
#####################################################
  
def flip_column():
  x = ""
  while x not in column_number:#determine which column to flip
    x = column_input
  x = column_number[x]
  
  for i in range(6):
    if column_input != column_list[i]: #iterate through column list
      continue   #until it hits the right column
    column = c[i]
    for i in range(6): # "flips" the column
      if column[i] == 1:
        column[i] = 0
      elif column[i] == 0:
        column[i] = 1
      r[i][x] = column[i] #make rows = to columns
  return ""
#####################################################

print("\n\n This program is called Waffle and to solve it you have to flip \n either a row or a column until the whole side is one color. \n\n") 


while True:

  if solved == True:
    solved = False #Shuffle
    shuffle_waffle()
  
  output()

  row_input = ""
  column_input = ""
#choose row(s) to flip
  RC = input("Do you want to flip a row or a column? (R/C): ")
  if RC.upper() == "R":
    while row_input not in row_list:
      row_input = input("Which row do you want to flip? (r1-r6): ")
    row_input = row_input.lower()
    print(flip_row())
#choose column(s) to flip
  elif RC.upper() == "C":
    while column_input not in column_list:
      column_input = input("Which column do you want to flip? (c1-c6): ")
    column_input = column_input.lower()
    print(flip_column())
#Repeat program
  if(r1 == r2 == r3 == r4 == r5 == r6):
    print("You Solved It!")
    solved = True
    again = input(" Play again? (Y/N)")
    if again[0].upper() == "N": 
      break
    