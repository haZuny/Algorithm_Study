import sys

n = int(sys.stdin.readline())
pure = []
list = list(map(int, sys.stdin.readline().split()))

for num in list:
    if not num in pure:
        pure.append(num)
        
pure.sort()

for num in list:
    print(pure.index(num), end=' ')
