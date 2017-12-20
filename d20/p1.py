#!/usr/bin/env python3
import sys

def main(ln):
  p, v, a = ln.split()
  p, v, a = map(lambda x: x[x.index('<') + 1:], [p, v, a])
  p, v, a = map(lambda x: x[:x.index('>')], [p, v, a])
  p, v, a = map(lambda x: x.split(','), [p, v, a])
  p, v, a = map(lambda x: list(map(int, x)), [p, v, a])
  return (p, v, a)

which = -1
minmana = float('inf')
for i, line in enumerate(sys.stdin):
  pt = main(line.strip())
  a = pt[2]
  mana = sum(map(abs, a))
  if mana < minmana:
    minmana = mana
    which = i
print(which)
