#!/usr/bin/env python3
import sys

def main(i, stc, regs, n):
  v1 = 0
  v2 = 0
  try:
    v2 = int(stc[2])
  except ValueError:
    if stc[2] not in regs:
      regs[stc[2]] = 0
    v2 = regs[stc[2]]
  s = stc[0]
  a = stc[1]
  try:
    v1 = int(a)
  except ValueError:
    if a not in regs:
      regs[a] = 0
    v1 = regs[a]
  if s == 'set':
    regs[a] = v2
  elif s == 'sub':
    regs[a] -= v2
  elif s == 'mul':
    regs[a] *= v2
    n[0] += 1
  elif s == 'jnz':
    if v1 != 0:
      return i + v2
  return i + 1

regs = {}
stcs = []
for line in sys.stdin:
  stcs.append(line.split())

i = 0
count = 0
n = [0]
while i >= 0 and i < len(stcs):
  i = main(i, stcs[i], regs, n)
print(n[0])
