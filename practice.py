import sys
import math

a = int(input())

for i in range(a):

    height, side, n = map(int, sys.stdin.readline().split())

    cnt = 0
    up = 1
    side = 1

    while True:
        cnt += 1

        if len(str(side)) == 1:
            side = "0" + str(side)

        else:
            side = str(side)

        num = str(up) + side

        side = int(side)

        if up%height == 0:
            up = 0
            side += 1

        if cnt == n:
            break

        up += 1

    print(num)