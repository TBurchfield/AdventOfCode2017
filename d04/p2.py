#!/usr/bin/env python3
import sys

def ana(s1, s2):
  chars = {}
  charlist = []
  for c1 in s1:
    if c1 in chars:
      chars[c1] += 1
    else:
      chars[c1] = 1
      charlist.append(c1)
  chars2 = {}
  charlist2 = []
  for c2 in s2:
    if c2 in chars2:
      chars2[c2] += 1
    else:
      chars2[c2] = 1
      charlist2.append(c2)
  flag = True
  for c1 in charlist:
    if not c1 in chars2:
      flag = False
    elif chars2[c1] != chars[c1]:
      flag = False

  for c2 in charlist2:
    if not c2 in chars:
      flag = False
    elif chars2[c2] != chars[c2]:
      flag = False
  return flag

amt = 0
for line in sys.stdin:
  words = line.split()
  stuff = []
  flag = True
  for word in words:
    for found in stuff:
      if ana(word, found):
        flag = False
    stuff.append(word)
  if flag:
    amt += 1
print(amt)
