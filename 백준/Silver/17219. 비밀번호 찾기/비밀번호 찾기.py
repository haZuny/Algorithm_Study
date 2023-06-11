import sys

n, m = map(int, sys.stdin.readline().split())
dict = {}
for _ in range(n):
    addr, password = sys.stdin.readline().split()
    dict[addr] = password
for _ in range(m):
    addr = sys.stdin.readline()[:-1]
    print(dict[addr])