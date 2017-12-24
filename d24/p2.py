#!/usr/bin/env python3
import sys

def rest_of(path, visited, comps, length, strength):
  bestpath = []
  lmax = 0
  stmax = 0
  for i, comp in enumerate(comps):
    if i in visited:
      continue
    if path[-1][1] == comp[0]:
      visited.add(i)
      attempt, st = rest_of(path + [comp], visited, comps, length + 1, strength + comp[0] + comp[1])
      st += comp[0] + comp[1]
      attempt += 1
      if attempt > lmax or (attempt == lmax and  st > stmax):
        lmax = attempt
        stmax = st
      visited.remove(i)
    elif path[-1][1] == comp[1]:
      visited.add(i)
      attempt, st = rest_of(path + [comp[::-1]], visited, comps, length + 1, strength + comp[0] + comp[1])
      st += comp[0] + comp[1]
      attempt += 1
      if attempt > lmax or (attempt == lmax and  st > stmax):
        lmax = attempt
        stmax = st
      visited.remove(i)
  return [lmax, stmax]

comps = [] #the zero port
for line in sys.stdin:
  comps.append(list(map(int, line.strip().split('/'))))

visited = set()
length, strength = rest_of([[0,0]], visited, comps, 0, 0)
print(strength)
