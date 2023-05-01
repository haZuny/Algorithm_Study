import sys

# 물품의 수, 버틸수 있는 무게 입력
n, k = map(int, sys.stdin.readline().split())

# 각 물건의 무게, 해당 물건의 가치 입력
toys = []
for i in range(n):
    toys.append(list(map(int, sys.stdin.readline().split())))
    
# list[검사한 물건 수][남은 공간] 정의
list = [[0 for j in range(k+1)] for i in range(n+1)]

for k_ in range(1, k+1):
    for n_ in range(1, n+1):
        # 검사하는 물건의 무게 > 남은 공간의 경우
        if toys[n_-1][0] > k_:
            list[n_][k_] = list[n_-1][k_]
        else:
            list[n_][k_] = max(list[n_-1][k_], list[n_-1][k_-toys[n_-1][0]] + toys[n_-1][1])

print(list[n][k])

