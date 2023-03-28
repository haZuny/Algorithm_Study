import sys

n = int(sys.stdin.readline())
max = n // 5
rest = n % 5

for i in range(max, -1, -1):
    if rest % 3 == 0:
        print(max + rest // 3)
        break
    else:
        max -= 1
        rest += 5
if(max < 0):
    print(-1)
