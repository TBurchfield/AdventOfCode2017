#!/usr/bin/env python3
import sys

severity = 0
#FINISHED, do not edit 
for line in sys.stdin:
  line = line.split()
  depth = int(line[0][:-1])
  ran = int(line[1])
  cycle = ran*2 - 2
  if (depth % cycle == 0):
    severity += depth*ran

print(severity)
