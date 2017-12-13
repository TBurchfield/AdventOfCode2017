#!/usr/bin/env python3
import sys
cd = []
for line in sys.stdin:
  line = line.split()
  depth = int(line[0][:-1])
  ran = int(line[1])
  cycle = ran*2 - 2
  cd.append([cycle, depth])

severity = 0
delay = -1
winning = False
while not winning:
  delay += 1
  winning  = True
  for pair in cd:
    depth = pair[1] + delay
    cycle = pair[0]
    if (depth % cycle == 0):
      winning = False

print(delay)
