import sys

n = int(sys.stdin.readline())
for i in range(n):
    myList = list(map(int, sys.stdin.readline().split()))
    # 평균 구하기
    add = 0
    for i in myList[1:]:
        add += i
    aver = add / myList[0]
    # 비율 구하기
    cnt = 0
    for i in myList[1:]:
        if i > aver:
            cnt += 1
    print('%.3f%%'%round(cnt / myList[0] * 100, 3))