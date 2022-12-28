import sys

# input() 보다 sys.stdin.readline() 이 훨씬 빠르다.
t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)