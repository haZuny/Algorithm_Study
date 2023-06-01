import sys

n, m = map(int, sys.stdin.readline().split())
graph = {}
for i in range(1, n+1):
    graph[i] = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 모든 노드를 방문 할 때 까지 그래프 순회(DFS)
unsearched = [i for i in range(1, n+1)]
stack = []
groupCnt = 0

while unsearched:
    # 스택이 비어있으면 방문 안한 노드부터 다시 탐색, 카운트 증가
    if not stack:
        stack.append(unsearched[0])
        groupCnt += 1
    else:
        current = stack.pop()
        unsearched.remove(current)
        for node in graph[current]:
            if node in unsearched and not node in stack:
                stack.append(node)

print(groupCnt)
