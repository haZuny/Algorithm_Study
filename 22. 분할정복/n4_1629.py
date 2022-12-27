from sys import stdin
a, b, c = map(int, stdin.readline().split())

def getNum(a, b):
    if b == 1:
        return a % c
    if b % 2 == 0:
        return getNum(a, b//2)**2 % c
    else:
        return (getNum(a, b//2)**2 * a) % c

print(getNum(a,b))