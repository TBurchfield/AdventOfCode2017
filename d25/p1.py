#!/usr/bin/env python3

states = {'a':[[1,1,'b'],[0,-1,'c']],
          'b':[[1, -1, 'a'],[1, 1, 'd']],
          'c':[[0, -1, 'b'],[0, -1, 'e']],
          'd':[[1, 1, 'a'],[0, 1, 'b']],
          'e':[[1, -1, 'f'],[1, -1, 'c']],
          'f':[[1, 1, 'd'],[1, 1, 'a']],
          }
s = 'a'
tape = {}
on = 0
for _ in range(12667664):
  un = 0
  if on not in tape or tape[on] == 0:
    un = 0
  else:
    un = 1
  tape[on] = states[s][un][0]
  on += states[s][un][1]
  s = states[s][un][2]

#sum
add = 0
for on in tape.keys():
  if tape[on] == 1:
    add += 1
print(add)
