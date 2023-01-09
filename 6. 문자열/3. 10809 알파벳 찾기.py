import sys

s = sys.stdin.readline()

start = ord('a')
for i in range(start, start+26):
    if chr(i) in s:       
        print(s.index(chr(i)),'', end='')
    else:
        print(-1,'', end='')

