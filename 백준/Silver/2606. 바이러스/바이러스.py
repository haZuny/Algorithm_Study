computers = int(input())
networks = int(input())

graph = {}

for i in range(1, computers+1):
    graph[i] = set()
    
for _ in range(networks):
    i, j = map(int, input().split())
    graph[i].add(j)
    graph[j].add(i)

# 그래프 dfs 순회하면서 1번 컴과 연결된 컴퓨터 탐색
cnt = 0
visited = []
stack = [1]
    
while len(stack) > 0:
    cnt += 1
    current = stack.pop()
    visited.append(current)
    for i in graph[current]:
        if not i in visited:
            stack.append(i)
            visited.append(i)
            
print(cnt-1)
