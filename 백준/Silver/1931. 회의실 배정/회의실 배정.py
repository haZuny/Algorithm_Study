import sys

n = int(input())

lst = []
num = 0

# 리스트 초기화
for _ in range(n):
    lst.append(tuple(map(int, sys.stdin.readline().split())))

# 끝나는 시간 기준 정렬
lst.sort(key=lambda t: (t[1], t[0]))

lastEnd = 0
for s, e in lst:
    if s >= lastEnd:
        num += 1
        lastEnd = e

print(num)
