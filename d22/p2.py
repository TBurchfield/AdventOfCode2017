#!/usr/bin/env python3
import sys

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def burst(n, board):
  count = 0
  x = 0
  y = 0
  d = 0 #up
  for i in range(n):
    if i % 1000 == 0:
      print('{}%'.format(i*100/n))
    if (x,y) not in board or board[(x,y)] == '.':
      d = (d - 1) % len(dirs)
      board[(x,y)] = 'w'
    elif board[(x,y)] == 'w':
      count += 1
      board[(x,y)] = '#'
    elif board[(x,y)] == '#':
      d = (d + 1) % len(dirs)
      board[(x,y)] = 'f'
    elif board[(x,y)] == 'f':
      d = (d + 2) % len(dirs)
      board[(x,y)] = '.'
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

print(burst(10000000, board))
