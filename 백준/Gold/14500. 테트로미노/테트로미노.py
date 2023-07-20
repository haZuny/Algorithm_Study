n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

# DFS로 순회, 길이 4가 되면 합 계산
# (x, y, size, route, sum)
stack = []
for i in range(n):
    for j in range(m):
        stack.append((i, j, 1, [(i, j)], board[i][j]))

maxSum = 0

while stack:
    x, y, size, route, sum = stack.pop()

    if size == 4:
        maxSum = max(sum, maxSum)
    else:
        if x > 0 and (x-1, y) not in route:
            stack.append((x-1, y, size+1, route+[(x-1, y)], sum+board[x-1][y]))
        if x < n-1 and (x+1, y) not in route:
            stack.append((x+1, y, size+1, route+[(x+1, y)], sum+board[x+1][y]))
        if y > 0 and (x, y-1) not in route:
            stack.append((x, y-1, size+1, route+[(x, y-1)], sum+board[x][y-1]))
        if y < m-1 and (x, y+1) not in route:
            stack.append((x, y+1, size+1, route+[(x, y+1)], sum+board[x][y+1]))

        # 메산 모양 폴리오미노 고려
        if size == 3:
            midx, midy = route[1]
            # 상하 메산
            if x == midx:
                if midy > 0 and (x, midy-1) not in route:
                    stack.append((x, midy-1, size+1, route+[(x, midy-1)], sum+board[x][midy-1]))
                if midy < m-1 and (x, midy+1) not in route:
                    stack.append((x, midy+1, size+1, route+[(x, midy+1)], sum+board[x][midy+1]))
            # 좌우 메산
            else:
                if midx > 0 and (midx-1, y) not in route:
                    stack.append((midx-1, y, size+1, route+[(midx-1, y)], sum+board[midx-1][y]))
                if midx < n-1 and (midx+1, y) not in route:
                    stack.append((midx+1, y, size+1, route+[(midx+1, y)], sum+board[midx+1][y]))

print(maxSum)
