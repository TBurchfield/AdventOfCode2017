#!/usr/bin/env python3
import sys

amt = 0
for line in sys.stdin:
  words = line.split()
  stuff = {}
  flag = True
  for word in words:
    if word in stuff:
      flag = False
    stuff[word] = True
  if flag:
    amt += 1
print(amt)
