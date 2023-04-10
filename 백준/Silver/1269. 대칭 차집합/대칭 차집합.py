import sys

a, b = map(int, sys.stdin.readline().split())
set_a = set(sys.stdin.readline().split())
set_b = set(sys.stdin.readline().split())

set_amb = set_a - set_b
set_bma = set_b - set_a
print(len(set_amb | set_bma))
