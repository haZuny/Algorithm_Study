n, m = map(int, input().split())
# 케인 베이컨의 수
kebinList = [[float('inf') for _ in range(n+1)] for _ in range(n)]
# 그래프 초기화
graph = {}
for i in range(n):
    graph[i] = []
for _ in range(m):
    u1, u2 = map(int, input().split())
    graph[u1-1].append(u2-1)
    graph[u2-1].append(u1-1)

# bfs 탐색
import collections

for i in range(n):
    queue = collections.deque([(i, 0)])
    searched = set([i])

    while(queue):
        current, kebin  = queue.popleft()
        kebinList[i][current] = kebin+1

        for node in graph[current]:
            if node not in searched:
                queue.append((node, kebin+1))
                searched.add(node)

        kebinSum = 0
        for j in range(n):
            if i == j:
                pass
            kebinSum += kebinList[i][j]
        kebinList[i][-1] = (kebinSum, i)

# 제일 작은 값 찾기
minKebin = (float('inf'),float('inf'))
for i in range(n):
    minKebin = min(minKebin, kebinList[i][-1])
    
print(minKebin[1]+1)