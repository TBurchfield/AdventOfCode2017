#!/usr/bin/env python3
import sys
def follow(mat):
  dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
  letters = []
  d = 0 # up
  i = 0
  j = 0
  n = 0
  for x, char in enumerate(mat[0]):
    if char == "|":
      j = x
  end = False
  while not end:
    n += 1
    ci = i + dirs[d][0]
    cj = j + dirs[d][1]
    if ci < len(mat) and ci >= 0 and cj < len(mat[ci]) and cj >= 0 and mat[ci][cj] != ' ':
      #keep moving forward
      if mat[ci][cj].isalpha():
        letters.append(mat[ci][cj])
      i = ci
      j = cj
    else:
      d = (d - 1) % 4
      ci = i + dirs[d][0]
      cj = j + dirs[d][1]
      if ci < len(mat) and ci >= 0 and cj < len(mat[ci]) and cj >= 0 and mat[ci][cj] != ' ':
        #turn left
        if mat[ci][cj].isalpha():
          letters.append(mat[ci][cj])
        i = ci
        j = cj
      else:
        d = (d + 2) % 4
        ci = i + dirs[d][0]
        cj = j + dirs[d][1]
        if ci < len(mat) and ci >= 0 and cj < len(mat[ci]) and cj >= 0 and mat[ci][cj] != ' ':
          #turn right
          if mat[ci][cj].isalpha():
            letters.append(mat[ci][cj])
          i = ci
          j = cj
        else:
          end = True
  return n
    

mat = []
for line in sys.stdin:
  mat.append(line.rstrip())
n = follow(mat)
print(n)
