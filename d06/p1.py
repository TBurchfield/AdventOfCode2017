#!/usr/bin/env python3
import sys

for line in sys.stdin:
  nums = list(map(int, line.split()))
  seen = set()
  dic = {}
  count = 0
  while not tuple(nums) in seen:
    seen.add(tuple(nums))
    dic[tuple(nums)] = count
    count += 1
    i = 0
    maxval = 0
    for j in range(len(nums)):
      if nums[j] > maxval:
        i = j
        maxval = nums[j]
    nums[i] = 0
    everyonegets = maxval // len(nums) #integer division
    overflow = maxval % len(nums)
    offsets = [(k + i) % len(nums) for k in range(1, overflow + 1)]
    for j in range(len(nums)):
      nums[j] += everyonegets
      if j in offsets:
        nums[j] += 1
  print(count)
  print(count - dic[tuple(nums)])
