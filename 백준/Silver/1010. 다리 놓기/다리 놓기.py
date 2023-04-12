import sys, math

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    top = 1
    bottom = math.factorial(n)

    for i in range(m, m-n, -1):
        top *= i
    print(top//bottom)
