import sys

a1, a2 = map(int, sys.stdin.readline().split())
b1, b2 = map(int, sys.stdin.readline().split())

c1 = a1 * b2 + b1 * a2
c2 = a2 * b2

temp = 2
while temp <= c1 and temp <= c2:
    if c1 % temp == 0 and c2 % temp == 0:
        c1 //= temp
        c2 //= temp
    else:
        temp += 1

print(c1, c2)
