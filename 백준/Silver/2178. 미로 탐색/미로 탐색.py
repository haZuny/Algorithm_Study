board = []
n, m = map(int, input().split())
for _ in range(n):
    board.append(input())

check = [[float('inf') for _ in range(m)] for _ in range(n)]

import collections
queue = collections.deque([(0,0,1)])
searched = set([0,0])

# bfs
while queue:
    x, y, cnt = queue.popleft()
    
    if x > n-1 or y > m-1 or x < 0 or y < 0:
        continue

    check[x][y] = min(cnt, check[x][y])

    if x > 0 and board[x-1][y] == '1' and ((x-1, y) not in searched):
        queue.append((x-1, y, cnt+1))
        searched.add((x-1, y))
    if x < n-1 and board[x+1][y] == '1' and ((x+1, y) not in searched):
        queue.append((x+1, y, cnt+1))
        searched.add((x+1, y))
    if y > 0 and board[x][y-1] == '1' and ((x, y-1) not in searched):
        queue.append((x, y-1, cnt+1))
        searched.add((x, y-1))
    if y < m-1 and board[x][y+1] == '1' and ((x, y+1) not in searched):
        queue.append((x, y+1, cnt+1))
        searched.add((x, y+1))
    
print(check[-1][-1])