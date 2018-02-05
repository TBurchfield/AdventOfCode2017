#!/usr/bin/env python3

# Programming challenge, for which the prompt is:
# http://adventofcode.com/2017/day/24

import sys

def rest_of(path, visited, comps, strength):
  smax = 0
  for i, comp in enumerate(comps):
    if i in visited:
      continue
    if path[-1][1] == comp[0]:
      visited.add(i)
      smax = max(smax, rest_of(path + [comp], visited, comps, strength + comp[0] + comp[1]) + comp[0] + comp[1])
      visited.remove(i)
    elif path[-1][1] == comp[1]:
      visited.add(i)
      smax = max(smax, rest_of(path + [comp[::-1]], visited, comps, strength + comp[0] + comp[1]) + comp[0] + comp[1])
      visited.remove(i)
  return smax

comps = [] #the zero port
for line in sys.stdin:
  comps.append(list(map(int, line.strip().split('/'))))

visited = set()
strength = rest_of([[0,0]], visited, comps, 0)
print(strength)
