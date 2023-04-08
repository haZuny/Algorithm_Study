import sys

l1, l2, l3 = map(int, sys.stdin.readline().split())
l_max = max(l1, l2, l3)
others = l1 + l2 + l3 - l_max
if others > l_max:
    print(l_max + others)
else:
    print(others * 2 - 1)
