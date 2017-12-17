#!/usr/bin/env python3
import sys

for line in sys.stdin:
  n = int(line.strip())
  vals = [0]
  i = 0
  for j in range(1, 2018):
    i = (i + n + 1) % len(vals)
    vals.insert(i, j)
  print(vals[(i + 1) % len(vals)])
