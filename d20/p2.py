#!/usr/bin/env python3
import sys

##############
# this is admittedly pretty sloppy.  You just wait for the value to stop changing.
##############

def step(parts, collided):
  seen = {}
  for i, part in enumerate(parts):
    p, v, a = part
    v[0] += a[0]
    v[1] += a[1]
    v[2] += a[2]
    p[0] += v[0]
    p[1] += v[1]
    p[2] += v[2]
    parts[i] = (p, v, a)

  for i, part in enumerate(parts):
    if i not in collided:
      p, v, a = part
      x, y, z = p
      if (x, y, z) not in seen:
        seen[(x, y, z)] = i
      elif seen[(x, y, z)] == None:
        collided.add(i)
      else:
        collided.add(seen[(x, y, z)])
        collided.add(i)
        seen[(x, y, z)] = None

def main(ln):
  p, v, a = ln.split()
  p, v, a = map(lambda x: x[x.index('<') + 1:], [p, v, a])
  p, v, a = map(lambda x: x[:x.index('>')], [p, v, a])
  p, v, a = map(lambda x: x.split(','), [p, v, a])
  p, v, a = map(lambda x: list(map(int, x)), [p, v, a])
  return (p, v, a)

parts = []
collided = set()

for i, line in enumerate(sys.stdin):
  parts.append(main(line.strip()))

while True:
  step(parts, collided)
  print(len(parts) - len(collided))
