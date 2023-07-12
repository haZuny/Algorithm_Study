import collections

m, n, h = map(int, input().split())

box = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(h)]

queue = collections.deque()
num0 = 0

for hi in range(h):
    for ni in range(n):
        for mi, v in enumerate(input().split()):
            v = int(v)
            box[hi][ni][mi] = v
            if v == 1:
                queue.append((mi, ni, hi, 0))
            elif v == 0:
                num0 += 1

# bfs
day = 0
while queue:
    current = queue.popleft()
    x, y, z, day = current
    # 6방향 탐색
    if x > 0 and box[z][y][x-1] == 0:
        box[z][y][x-1] = 1
        queue.append((x-1, y, z, day+1))
        num0 -= 1
    if x < m-1 and box[z][y][x+1] == 0:
        box[z][y][x+1] = 1
        queue.append((x+1, y, z, day+1))
        num0 -= 1

    if z > 0 and box[z-1][y][x] == 0:
        box[z-1][y][x] = 1
        queue.append((x, y, z-1, day+1))
        num0 -= 1
    if z < h-1 and box[z+1][y][x] == 0:
        box[z+1][y][x] = 1
        queue.append((x, y, z+1, day+1))
        num0 -= 1

    if y > 0 and box[z][y-1][x] == 0:
        box[z][y-1][x] = 1
        queue.append((x, y-1, z, day+1))
        num0 -= 1
    if y < n-1 and box[z][y+1][x] == 0:
        box[z][y+1][x] = 1
        queue.append((x, y+1, z, day+1))
        num0 -= 1

if num0 == 0:
    print(day)
else:
    print(-1)
