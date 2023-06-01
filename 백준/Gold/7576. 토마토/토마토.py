import sys, collections

m, n = map(int, sys.stdin.readline().split())

empty = set()
searched = set()
queue = collections.deque()

# 그래프에 삽입, 익은 토마토는 큐에 삽입
for i in range(n):
    for j, v in enumerate(map(int, sys.stdin.readline().split())):
        # 만약 익었으면 큐에 삽입
        if v == 1:
            queue.append((i, j, 0))
            searched.add((i, j))
        # 비어있으면 따로 분류
        elif v == -1:
            empty.add((i, j))

maxDay = -1

# bfs 탐색
while queue:
    # current 얻기
    i, j, day = queue.popleft()
    # 최대 날짜 갱신
    if day > maxDay: maxDay = day
    # 연결된 노드 탐색
    if i-1 >= 0 and (not (i-1, j) in empty) and (not (i-1, j) in searched):
        queue.append((i-1, j, day+1))
        searched.add((i-1, j))
    if i+1 < n and (not (i+1, j) in empty) and (not (i+1, j) in searched):
        queue.append((i+1, j, day+1))
        searched.add((i+1, j))
    if j-1 >= 0 and (not (i, j-1) in empty) and (not (i, j-1) in searched):
        queue.append((i, j-1, day+1))
        searched.add((i, j-1))
    if j+1 < m and (not (i, j+1) in empty) and (not (i, j+1) in searched):
        queue.append((i, j+1, day+1))
        searched.add((i, j+1))

# 출력
if len(searched)+len(empty) == m*n:
    print(maxDay)
else:
    print(-1)
