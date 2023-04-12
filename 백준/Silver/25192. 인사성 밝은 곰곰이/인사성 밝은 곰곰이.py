import sys

sSet = set()
cnt = 0
n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline()[:-1]
    if s == "ENTER":
        sSet = set()
    else:
        if not s in sSet:
            cnt += 1
            sSet.add(s)
print(cnt)
