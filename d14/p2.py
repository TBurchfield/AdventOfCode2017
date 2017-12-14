#!/usr/bin/env python3
import sys

def mark(r, c, seen, mat):
  front = [[r, c]]
  seen.add(tuple([r, c]))
  while len(front) > 0:
    which = front.pop()
    for diff in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
      x, y = [which[0] + diff[0], which[1] + diff[1]]
      if (tuple([x, y]) not in seen) and x >= 0 and y >= 0 and x < len(mat) and y < len(mat[0]):
        if mat[x][y] == '1':
          seen.add(tuple([x, y]))
          front.append([x, y])

def count(mat):
  seen = set()
  n = 0
  for r, row in enumerate(mat):
    for c, item in enumerate(row):
      if tuple([r,c]) in seen:
        continue
      if item == '1':
        mark(r, c, seen, mat)
        n += 1
  return n

def f(a, m):
  knot = [i for i in range(m)]
  skip = 0
  i = 0
  for _ in range(64):
    for n in a:
      part2 = knot[: max(n - m + i, 0)]
      part = knot[i:min(i + n, m)] #size can be m - i
      parts = part + part2
      parts = parts[::-1]
      knot[i:min(i + n, m)] = parts[:m - i]
      knot[: max(n - m + i,0)] = parts[m - i:]
      i = (i + n + skip) % m #fence?
      skip += 1
  dense = ""
  val = -1
  for j in range(16):
    for k in range(16):
      if k == 0:
        val = knot[(j*16) + k]
      else:
        val ^= knot[(j*16) + k]
    dense += format(val, '02x')
  return dense

for line in sys.stdin:
  matr = [[i for i in f(list(map(ord,line.strip() + "-" + str(row))) + [17, 31, 73, 47, 23], 256)] for row in range(128)]
  mat = []
  for i, row in enumerate(matr):
    mat.append([])
    for item in row:
      for bit in format(int(item, 16), "#06b")[2:]:
        mat[i].append(bit)
  n = count(mat)
  print(n)
