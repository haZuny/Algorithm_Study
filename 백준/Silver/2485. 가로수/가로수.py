import sys

n = int(sys.stdin.readline())

trees = []

for _ in range(n):
    trees.append(int(sys.stdin.readline()))
trees.sort()

mm = trees[1] - trees[0]
gabs = [mm]
last = trees[1]

for i in range(2, n):
    gab = trees[i] - last
    gabs.append(gab)
    last = trees[i]

    check = 1
    for j in range(1, mm+1):
        if mm % j == 0 and gab % j == 0:
            check = j
    mm = check

answer = 0

for gab in gabs:
    answer += gab//mm - 1
    
print(answer)
