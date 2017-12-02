#!/usr/bin/env python3
import sys

x = 0
for line in sys.stdin:
  line = [int(v) for v in line.split()]
  found = False
  for i in range(len(line)):
    for j in range(len(line)):
      if i == j:
        continue
      if line[i] % line[j] == 0 and not found:
        x += line[i] / line[j]
        found = True
print(x)
