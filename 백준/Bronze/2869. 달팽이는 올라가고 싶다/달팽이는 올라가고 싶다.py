import sys

a, b, v = map(int, sys.stdin.readline().split())

pure = a - b
point = ((v-a) // pure)
if(v - point * pure <= a):
    print(point + 1)
else:
    print(point + 2)
