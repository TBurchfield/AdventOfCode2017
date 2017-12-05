#!/usr/bin/env python3
import sys
import math
memo = {1: 1, 2:1, 3:2, 4:4, 5:5, 6:10, 7:11, 8:23, 9:25}

def adt(a, b):
  x = []
  for i in range(len(a)):
    x.append(a[i] + b[i])
  return tuple(x)

def to(target):
  pts = {(0,0):1, (1,0):1}
  drs = [(0,1), (-1,0), (0,-1), (1,0)]
  alldrs = [(i,j) for i in [-1,0,1] for j in [-1,0,1]]
  dr = 1 #0 is up, 1 left, 2 down, 3 right
  at = (1,1)
  num = 3
  ring = 3
  howmany = 0
  while True:
    if dr == 0:
      go = ring - 2
    elif dr == 3:
      go = ring
    else:
      go = ring - 1
    for _ in range(go):
      #update at
      pts[at] = sum([(pts[adt(x, at)] if adt(x,at) in pts else 0) for x in alldrs])
      #check at
      if pts[at] > target:
        return [num, pts[at]]
      #inc at, num
      at = adt(at, drs[dr])
      num += 1
    dr = (dr + 1) % 4
    if dr == 0:
      ring += 2

for x in sys.stdin:
  x = int(x)
  print("{} exceeded at {} by {}'th".format(x,*to(x)))
