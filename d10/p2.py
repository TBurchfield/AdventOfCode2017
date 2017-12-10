#!/usr/bin/env python3
import sys

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
  #return val
  return dense

for line in sys.stdin:
  print(f(list(map(ord,line.strip())) + [17, 31, 73, 47, 23], 256))
