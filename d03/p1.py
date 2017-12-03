#!/usr/bin/env python3
import sys
import math
memo = {1: 1, 2:1, 3:2, 4:4, 5:5, 6:10, 7:11, 8:23, 9:25}

def ret(x):
  if x in memo:
    return memo[x]
  on = int(math.floor(math.sqrt(x - 1)))
  if on % 2 == 0:
    on -= 1
  on += 2
  along = int(x - pow(on - 2, 2))
  mid = (on-1)/2
  toReturn = 0
  corn = along % (on - 1)
  prevcirc = pow((on - 4), 2) + along - 1
  if along <= (on - 1):
    pass
  elif along <= (on - 1)*2:
    prevcirc -= 2
  elif along <= (on - 1)*3:
    prevcirc -= 4
  elif along < (on - 1)*4:
    prevcirc -= 6

  if corn == 0: #corner
    print("{} is a corner".format(x))
    return ret(x - 1) + ret(prevcirc - 1)
  if corn == 1: #aftercorner
    print("{} is after corner".format(x))
    return ret(x - 1) + ret(prevcirc + 1) + ret(prevcirc)
  if corn == on - 2: #beforecorner
    print("{} is before corner".format(x))
    return ret(x - 1) + ret(prevcirc - 1) + ret(prevcirc)
  else:
    print("{} is normal".format(x))
    return ret(x - 1) + ret(prevcirc - 1) + ret(prevcirc) + ret(prevcirc + 1)

'''
for x in sys.stdin:
  x = int(x.split()[0])
'''
for x in range(9,15):
  ret(x)
