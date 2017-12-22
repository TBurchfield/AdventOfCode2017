#!/usr/bin/env python3
import sys

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def burst(n, board):
  count = 0
  x = 0
  y = 0
  d = 0 #up
  for i in range(n):
    if (x,y) in board and board[(x,y)] == '#':
      d = (d + 1) % len(dirs)
      board[(x,y)] = '.'
    else:
      d = (d - 1) % len(dirs)
      board[(x,y)] = '#'
      count += 1
    x += dirs[d][0]
    y += dirs[d][1]
  return count

board = {}
size = 25
y = (size - 1) / 2
x = -(size - 1) / 2
for line in sys.stdin:
  line = line.strip()
  for c in line:
    board[(x,y)] = c
    x += 1
  x = -(size - 1) / 2
  y -= 1

print(burst(10000, board))
