#!/usr/bin/env python3
import sys

for line in sys.stdin:
  line = line.strip()
  x = 0
  line += line[0]
  for i in range(len(line) - 1):
    if line[i + 1] == line[i]:
      x += int(line[i]) 
  print(x)
