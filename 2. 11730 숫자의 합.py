import sys

n = int(sys.stdin.readline())
numLs = sys.stdin.readline()

sum = 0
for i in numLs[:-1]:
    sum += int(i)
print(sum)
