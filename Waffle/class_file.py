# Name: Waffle Classes
# Author: Owen Maguire
# Date: 1/31/23
# Desc: Classes/Objects used in "Waffle"
# Location: Beaverton High School, Oregon
#####################################################
class Shuffle:

  def __init__(self, line):
    self.line = line

  def shuffle(self):
    import random

    for i in range(6):
      rnum = random.randint(0,1)
      self.line[i] = rnum 
    return ""
#####################################################
class Flip_Row:
  pass
#####################################################
class Flip_Column:
  pass