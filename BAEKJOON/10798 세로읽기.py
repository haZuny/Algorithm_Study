import sys

arr = []
maxCnt = 0

for _ in range(5):
    str = sys.stdin.readline()[:-1]
    if len(str) > maxCnt:
        maxCnt = len(str)
    arr.append(str)

s = ""
for j in range(maxCnt):
    for i in range(5):
        try:
            s += arr[i][j]
        except:
            pass
print(s)
