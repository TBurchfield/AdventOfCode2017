#!/usr/bin/env python3
import sys

def spin(action, programs):
  n = int(action)
  begin = programs[len(programs) - n:]
  end = programs[:len(programs) - n]
  return begin + end

def exchange(action, programs):
  a, b = map(int, action.split('/'))
  x = programs[a]
  y = programs[b]
  return partner("{}/{}".format(x, y), programs)

def partner(action, programs):
  a, b = action.split('/')
  programs = programs.replace(a,'!')
  programs = programs.replace(b,a)
  programs = programs.replace('!',b)
  return programs

for line in sys.stdin:
  programs = 'abcdefghijklmnop'
  line = line.strip().split(',')
  nruns = 1000000000
  follow = {}
  for i in range(nruns):
    if i % 10000 == 0:
      print('{}%'.format((i*100)/nruns))
    if programs in follow:
      programs = follow[programs]
    else:
      start = programs
      for action in line:
        a = action[0]
        if a == 's':
          programs = spin(action[1:], programs)
        if a == 'x':
          programs = exchange(action[1:], programs)
        if a == 'p':
          programs = partner(action[1:], programs)
      follow[start] = programs
  print(programs)
