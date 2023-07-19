import collections

n, m = map(int, input().split())
graph = {}

for i in range(1, 101):
    graph[i] = i

# 사다리 입력
for _ in range(n):
    x, y = map(int, input().split())
    graph[x] = y

# 뱀 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u] = v

# bfs 탐색
queue = collections.deque()
queue.append((1, 0))
searched = set([1])

while queue:
    current, cnt = queue.popleft()
    for i in range(1, 7):
        try:
            if graph[current+i] not in searched:
                queue.append((graph[current+i], cnt+1))
                searched.add(graph[current+i])
        except:
            pass

    if current == 100:
        print(cnt)
        break