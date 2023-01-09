import sys

s = sys.stdin.readline()[:-1]
s = s.strip()
if s == "":
    print(0)
else:
    print(s.strip().count(' ') + 1)

