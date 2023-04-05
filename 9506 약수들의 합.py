import sys

while True:
    n = int(sys.stdin.readline())
    # 종료
    if n == -1:
        break
    checker = 0
    sum = 0
    list = []
    # 약수 체
    while checker < n-1:
        checker += 1
        if n % checker == 0:
            list.append(checker)
            sum += checker
    if sum == n:
        print(n, '=', end=' ')
        print(list[0], end='')
        for i in range(1, len(list)):
            print(' +', list[i], end="")
        print()
    else:
        print(f'{n} is NOT perfect.')
