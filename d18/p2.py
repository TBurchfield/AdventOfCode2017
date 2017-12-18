#!/usr/bin/env python3
import sys
import time
import queue



def main(line, regs, sndqueue, rcvqueue, i, pid, n):
  inst = line[0]
  reg = line[1]
  val = 0
  val1 = 0
  if len(line) == 3:
    val = line[2]
    try:
      val = int(val)
    except ValueError:
      if val not in regs:
        regs[val] = 0
      val = regs[val]
  else:
    val1 = line[1]
    try:
      val1 = int(val1)
    except ValueError:
      if val1 not in regs:
        regs[val1] = 0
      val1 = regs[val1]

  jumpval = 0
  try:
    int(reg)
    jumpval = int(reg)
  except ValueError:
    if reg not in regs:
      regs[reg] = 0
    jumpval = regs[reg]

  if inst == 'set':
    regs[reg] = val
  elif inst == 'add':
    regs[reg] += val
  elif inst == 'mul':
    regs[reg] *= val
  elif inst == 'mod':
    regs[reg] = regs[reg] % val
  elif inst == 'rcv':
    if rcvqueue.empty():
      return i
    else:
      regs[reg] = rcvqueue.get()
      return i + 1
  elif inst == 'snd':
    if pid == 1:
      n[0] += 1
    sndqueue.put(val1)
  elif inst == 'jgz':
    if jumpval > 0:
      return i + val
  return i + 1

structs = []
n = [0]
useless = [0]
regs0 = {'p': 0}
regs1 = {'p': 1}
rcv0 = queue.Queue()
rcv1 = queue.Queue()
term0 = False
term1 = False
for line in sys.stdin:
  structs += [line.split()]

i0 = 0
i0p = -1
i1 = 0
i1p = -1
while not (term0 and term1):
  #time.sleep(0.1)
  '''
  print('---------')
  print(term0, term1)
  print(rcv0, rcv1)
  print(i0, i1)
  print(structs[i0], structs[i1])
  print('---------')
  '''
  if i0 == i0p and i1 == i1p:
    break
  i0p = i0
  i1p = i1
  if not term0:
    i0 = main(structs[i0], regs0, rcv1, rcv0, i0, 0, useless)
  if not term1:
    i1 = main(structs[i1], regs1, rcv0, rcv1, i1, 1, n)

  if i0 >= len(structs) or i0 < 0:
    term0 = True
  if i1 >= len(structs) or i1 < 0:
    term1 = True

print(n[0])
