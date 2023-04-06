import sys

t = int(sys.stdin.readline())
for repeat in range(t):
    s = sys.stdin.readline()
    print(s[0]+s[-2])
