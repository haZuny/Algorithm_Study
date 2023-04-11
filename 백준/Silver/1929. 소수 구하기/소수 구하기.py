import sys, math

m, n = map(int, sys.stdin.readline().split())

for i in range(max(2, m), n+1):
    sosu = True
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            sosu = False
            break
    if sosu:
        print(i)
