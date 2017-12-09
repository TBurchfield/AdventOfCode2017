#!/usr/bin/env python3
import sys

for line in sys.stdin:
  c = line.strip()
  i = 0
  lvl = 0
  score = 0
  g = False

  while i < len(c):
    if not g:
      if c[i] == "<":
        g = True
      elif c[i] == "{":
        lvl += 1
      elif c[i] == "}":
        score += lvl
        lvl -= 1
    else:
      if c[i] == "!":
        i += 1
      elif c[i] == ">":
        g = False
    i += 1
  print(score)
