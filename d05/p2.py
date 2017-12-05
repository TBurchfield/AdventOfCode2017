#!/usr/bin/env python3
import sys

ins = []
for line in sys.stdin:
  ins.append(int(line))
at = 0
proc = 0
while at >= 0 and at < len(ins):
  to = at + ins[at]
  if ins[at] > 2:
    ins[at] -= 1
  else:
    ins[at] += 1
  at = to
  proc += 1
print(proc)
