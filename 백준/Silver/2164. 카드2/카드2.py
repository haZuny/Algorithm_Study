import sys, collections

n = int(sys.stdin.readline())
cd = collections.deque()

for i in range(1, n+1):
    cd.append(i)

pop = True
while len(cd) != 1:
    if pop:
        cd.popleft()
        pop = False
    else:
        temp = cd.popleft()
        cd.append(temp)
        pop = True

print(cd.pop())
