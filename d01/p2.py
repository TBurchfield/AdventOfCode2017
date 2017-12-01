#!/usr/bin/env python3
import sys

for line in sys.stdin:
  line = line.strip()
  n = len(line)
  x = 0
  line += line
  for i in range(n):
    if line[i + int(n/2)] == line[i]:
      x += int(line[i]) 
  print(x)
