'''
마지막 해: m과 n의 최대 공약수
k = m * ? + x = n * ?? + y
'''

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())

    # 최대공약수 구하기
    maxNum = 1
    mm, nn = m, n
    temp = 2
    while temp <= mm and temp <= nn:
        if mm % temp == 0 and nn % temp == 0:
            maxNum *= temp
            mm //= temp
            nn //= temp
        else:
            temp += 1
    maxNum *= mm
    maxNum *= nn

    possible = set()
    ans = -1
    
    # x 경우의 수 탐색
    x_possible = x
    while x_possible <= maxNum:
        possible.add(x_possible)
        x_possible += m

    # y 경우의 수 중 x와 겹치는 값 있으면 정답
    y_possible = y
    while y_possible <= maxNum:
        if y_possible in possible:
            ans = y_possible
            break
        y_possible += n

    print(ans)
