import sys, collections

n, m = map(int, sys.stdin.readline().split())

arr = [[0 for _ in range(m)] for _ in range(n)]
ans = [[-1 for _ in range(m)] for _ in range(n)]
goalRow = -1
goalColumn = -1

for i in range(n):
    for j, num in enumerate(map(int, sys.stdin.readline().split())):
        arr[i][j]=num
        if num == 2:
            goalRow = i
            goalColumn = j
        elif num == 0:
            ans[i][j] = 0
    
# BFS 탐색
# 목표 지점부터 옆칸 탐색
# arr[i, j] = min(arr[i, j], 넘겨받은 값)

queue = collections.deque()

queue.append((goalRow, goalColumn, -1))
searched = set([(goalRow, goalColumn)])

while queue:
    current = queue.popleft()
    row, col, val = current
    
    # 거리 업데이트
    ans[row][col] = val+1
    
    # 좌우상하 탐색
    if row > 0 and arr[row-1][col] != 0 and (row-1, col) not in searched :
        queue.append((row-1, col, val+1))
        searched.add((row-1, col))
        
    if  row < n-1 and arr[row+1][col] != 0 and (row+1, col) not in searched:
        queue.append((row+1, col, val+1))
        searched.add((row+1, col))
        
    if col > 0 and arr[row][col-1] != 0 and (row, col-1) not in searched:
        queue.append((row, col-1, val+1))
        searched.add((row, col-1))
        
    if col < m-1 and arr[row][col+1] != 0 and (row, col+1) not in searched:
        queue.append((row, col+1, val+1))
        searched.add((row, col+1))

for row in ans:
    print(" ".join(list(map(str, row))))
