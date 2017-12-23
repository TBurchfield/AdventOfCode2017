#!/usr/bin/env python3
import sys

def is_prime(a):
  return a > 1 and all(a % i for i in range(2, a))

top = 126300
bot = 109300
count = 0
while True:
  if not is_prime(bot):
    count += 1
  if bot == top:
    break
  bot += 17
print(count)
