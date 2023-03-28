import sys

n = int(sys.stdin.readline())


i = 2
while(i != n):
    if n % i == 0:
        print(i)
        n /= i
        i = 2
    elif n == 1:
        break
    else:
        i += 1
if (n != 1)
    print(int(n))
