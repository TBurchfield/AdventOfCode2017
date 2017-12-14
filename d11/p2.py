#!/usr/bin/env python3
import sys

ways = {'n':[0, 2],'s':[0, -2],'ne':[1,1],'nw':[-1, 1],'se':[1, -1],'sw':[-1, -1]}
def count(line):
  x = 0
  y = 0
  for element in line:
    x += ways[element][0]
    y += ways[element][1]
  return [abs(x),abs(y)]

def collapse(x, y):
  val = 0
  val += (y - x) // 2
  val += x
  return val

for line in sys.stdin:
  line = line.strip().split(',')
  furthest = 0
  for to in range(len(line)):
    x, y = count(line[:to + 1])
    dist = collapse(x, y)
    furthest = max(furthest, dist)
  print(furthest)
