#!/usr/bin/env python3
import sys

vals = {}
smal = float('-inf')
for line in sys.stdin:
  r, ud, v, word, condr, cond, condv = line.split()
  if not r in vals:
    vals[r] = 0
  if not condr in vals:
    vals[condr] = 0
  rhs = int(condv)
  lhs = vals[condr]
  if cond == ">":
    tru = lhs > rhs
  if cond == "<":
    tru = lhs < rhs
  if cond == "<=":
    tru = lhs <= rhs
  if cond == ">=":
    tru = lhs >= rhs
  if cond == "==":
    tru = lhs == rhs
  if cond == "!=":
    tru = lhs != rhs
  if tru:
    if ud=="inc":
      vals[r] += int(v)
    else:
      vals[r] -= int(v)
  if vals[r] > smal:
    smal = vals[r]

print(smal)
