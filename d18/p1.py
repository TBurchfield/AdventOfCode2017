#!/usr/bin/env python3
import sys



def main(line, regs, stack, i):
  inst = line[0]
  reg = line[1]
  val = 0
  if len(line) == 3:
    val = line[2]
    try:
      val = int(val)
    except ValueError:
      if val not in regs:
        regs[val] = 0
      val = regs[val]

  if reg not in regs:
    regs[reg] = 0
  if inst == 'set':
    regs[reg] = val
  elif inst == 'add':
    regs[reg] += val
  elif inst == 'mul':
    regs[reg] *= val
  elif inst == 'mod':
    regs[reg] = regs[reg] % val
  elif inst == 'rcv':
    if regs[reg] != 0:
      return [i + 1, stack.pop()]
  elif inst == 'snd':
    stack.append(regs[reg])
  elif inst == 'jgz':
    if regs[reg] > 0:
      return [i + val, None]
  return [i + 1, None]

structs = []
regs = {}
stack = []
for line in sys.stdin:
  structs += [line.split()]

i = 0
while True:
  i, freq = main(structs[i], regs, stack, i)
  if freq != None:
    print(freq)
    break
  if i >= len(structs) or i < 0:
    print(stack.pop())
    break
