import sys

n,m = map(int, sys.stdin.readline().split())

set_n = set()
for _ in range(n):
    set_n.add(sys.stdin.readline().strip())
    
set_m = set()
for _ in range(m):
    set_m.add(sys.stdin.readline().strip())

set_nm = set_n & set_m
list_nm = list(set_nm)
list_nm.sort()
print(len(set_nm))
for name in list_nm:
    print(name)
