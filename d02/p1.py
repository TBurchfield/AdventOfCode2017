#!/usr/bin/env python3
import sys

x = 0
for line in sys.stdin:
  line = [int(v) for v in line.split() ]
  a, i = [max(line), min(line)]
  x += a - i
print(x)
