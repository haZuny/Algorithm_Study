import collections

n, m, v = map(int, input().split())
graph = {}
for i in range(n):
    graph[i+1] = []

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# dfs
stack = [v]
searched = set()

while stack:
    current = stack.pop()
    if current in searched:
        continue
    searched.add(current)
    nest = graph[current]
    nest.sort(reverse=True)
    for node in nest:
        if node not in searched:
            stack.append(node)
    print(current, end= ' ')

print()
    
# bfs
queue = collections.deque([v])
searched = set()

while queue:
    current = queue.popleft()
    if current in searched:
        continue
    searched.add(current)
    nest = graph[current]
    nest.sort()
    for node in nest:
        if node not in searched:
            queue.append(node)
    print(current, end= ' ')
