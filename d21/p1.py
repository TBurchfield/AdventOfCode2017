#!/usr/bin/env python3
import sys

def rotate(mat): #rotates matrix
  new = []
  for i in range(len(mat[0])):
    new.append('')
    for row in mat:
      new[i] += row[i]
  return flip(new)

def pmat(mat):
  for row in mat:
    pass
    #print('${}$'.format(row))
  #print('')

def toslashes(mat):
  st = ''
  st += mat[0]
  for row in mat[1:]:
    st += '/'
    st += row
  return st

def flip(mat): #flips matrix down
  new = []
  for row in mat[::-1]:
    new.append(row)
  return new

def cell_replace(cell, rules):
  #print('entered cell_replace with:')
  pmat(cell)
  #print('--')
  ret = cell
  found = False
  for _ in range(5):
    cell = rotate(cell)
    if toslashes(cell) in rules:
      ret = rules[toslashes(cell)]
      found = True
  cell = flip(cell)
  for _ in range(5):
    cell = rotate(cell)
    if toslashes(cell) in rules:
      ret = rules[toslashes(cell)]
      found = True
  if not found:
    pass
    #print('cell replace failure')
  #print('leaving cell_replace with:')
  pmat(ret)
  #print('-- which has len {}'.format(len(ret)))
  return ret

def row_replace(row, rules):
  #print('entered row_replace (len: {}) with:'.format(len(row)))
  pmat(row)
  #print('--')
  if len(row) != 3 and len(row) != 2:
    #print('row_replace failure')
    return 'failure'
  l = 0
  if len(row) % 2 == 0:
    l = round((3/2)*len(row[0])) - 1
  else:
    l = round((4/3)*len(row[0])) - 1
  rot = flip(rotate(row)) #can now iterate by rows
  new = [' ' * (len(row) + 1) for _ in range(l)]
  #print('which flipped, is:')
  pmat(rot)
  newn = 0
  for i in range(0, len(rot), len(row)):
    #print('== rot is:')
    pmat(rot)
    #print('==')
    new[newn:newn + len(row) + 1] = cell_replace(rot[i:i+len(row)], rules)
    newn += len(row) + 1
  new = flip(rotate(new))
  #print('leaving row_replace with:')
  pmat(new)
  #print('--')
  return new

def replace(start, rules):
  #print('entering replace with:')
  pmat(start)
  #print('--')
  n = 0
  l = 0
  if len(start) % 2 == 0:
    n = 2
    l = round((3/2)*len(start)) - 1
  else:
    n = 3
    l = round((4/3)*len(start)) - 1
  #print('{} is n {} is len {} is l'.format(n, len(start), l))
  new = [' ' * l for _ in range(l)]
  oldn = 0
  newn = 0
  for i in range(0, len(start), n):
    new[newn:newn+(n+1)] = row_replace(start[oldn:oldn+n], rules)
    oldn += n
    newn += n + 1
  #print('leaving replace with:')
  pmat(new)
  #print('-- which has len {}'.format(len(new)))
  return new

start = \
['.#.',
 '..#',
 '###']
n = 5
rules = {}
for line in sys.stdin:
  i, o = line.strip().split(' => ')
  rules[i] = o.split('/')

for it in range(n):
  pmat(start)
  start = replace(start, rules)

on = 0
for row in start:
  for c in row:
    if c == '#':
      on += 1
print(on)
