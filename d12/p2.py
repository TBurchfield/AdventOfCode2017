#!/usr/bin/env python3
import sys

seen = set()

def count(to, start):
  start = str(start)
  seen.add(start)
  front = [start]
  c = 1
  while len(front) > 0:
    for thing in to[front.pop()]:
      if not thing in seen:
        seen.add(thing)
        c += 1
        front.append(thing)
  return c

to = {}
howmany = 0
for line in sys.stdin:
  line = line.split()
  fr = line[0]
  to[fr] = []
  howmany += 1
  for thing in line[2:]:
    if thing[-1] == ",":
      to[fr].append(thing[:-1])
    else:
      to[fr].append(thing)

g = 0
which = 0
while which < howmany:
  if str(which) in seen:
    which += 1
  else:
    g += 1
    count(to, which)

print(g)
