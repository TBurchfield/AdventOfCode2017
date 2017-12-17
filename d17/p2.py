#!/usr/bin/env python3
import sys

for line in sys.stdin:
  n = int(line.strip())
  i = 0
  recent = 0
  big = 1
  for j in range(1, 50000000):
    i = (i + n) % big
    i += 1
    if i == 1:
      recent = j
    big += 1
    if j % 1000 == 0:
      print("{}%".format(j*100/50000000))
  print(recent)
