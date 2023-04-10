import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    answer = 1
    num = 2
    while (num <= a and num <= b):
        if a % num == 0 and b % num == 0:
            answer *= num
            a //= num
            b //= num
        else:
            num += 1
        
    answer *= (a*b)
    print(answer)
