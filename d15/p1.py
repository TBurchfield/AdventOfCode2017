#!/usr/bin/env python3
import sys

sta = int(sys.stdin.readline().strip())
stb = int(sys.stdin.readline().strip())

fa = 16807
fb = 48271
mod = 2147483647
runs = 40000000
n = 0

for i in range(runs):
  sta = (sta * fa) % mod
  stb = (stb * fb) % mod
  bina = format(sta, "016b")[::-1]
  binb = format(stb, "016b")[::-1]
  bina = bina[:16]
  binb = binb[:16]
  if bina == binb:
    n += 1
  if i % 10000 == 0:
    print("{}%".format(100*i/runs))
print("count is {}".format(n))
