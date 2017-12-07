#!/usr/bin/env python3
import sys
processes = {}
procW = {}
proclist = []
children = {}
weightMemo = {}

def findWrong(root):
  ws = []
  for c in children[root]:
    ws.append(procW[c])

  for i, w in enumerate(ws):
    pass
    

def subtree_weight(root): #weight
  if root in weightMemo:
    return weightMemo[root]
  s = procW[root]
  for node in children[root]:
    s += subtree_weight(node)
  weightMemo[root] = s
  return s

def find_failing(root):
  print(root)
  if len(children[root]) > 0:
    if len(children) == 2:
      print("PANIC")
    val = subtree_weight(children[root][0])
    wrongs = []
    for c in children[root]:
      if subtree_weight(c) != val:
        wrongs.append(c)
    print(wrongs)
    wrong = "nothing"
    if len(wrongs) > 1:
      wrong = find_failing(children[root][0])
    elif len(wrongs) == 1:
      wrong = find_failing(wrongs[0])
    elif len(wrongs) == 0:
      return root
    return wrong
  return root

def fix(wrong):
  right = -1
  for bro in children[processes[wrong]]:
    if bro == wrong:
      continue
    right = subtree_weight(bro)
  new = right - (subtree_weight(wrong) - procW[wrong])
  print("right, sub, procw: {} {} {}".format(right, subtree_weight(wrong), procW[wrong]))
  return new

for line in sys.stdin:
  line = line.split()
  proc = line[0]
  pid = int(line[1][1:-1])
  procW[proc] = pid
  children[proc] = []
  if len(line) > 2:
    above = line[3:]
    for pro in above:
      x = pro
      if pro[-1] == ",":
        x=x[:-1]
      processes[x] = proc
      children[proc].append(x)
  proclist.append(proc)

root = "nothing"

for proc in proclist:
  if not (proc in processes):
    root = proc

print(fix(find_failing(root)))
