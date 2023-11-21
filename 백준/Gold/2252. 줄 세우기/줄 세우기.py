# 위상정렬 알고리즘을 이용하여 표기
# 리스트로 각 노드의 진입차수 표기
# 딕셔너리로 그래프 표현
# 매번 리스트를 순회하며 진입차수 0인 노드를 찾으면 시간 손실, set을 이용하여 문제 해결

import sys

n, m = map(int, sys.stdin.readline().split())

# 진입 차수
indegree = [0 for _ in range(n+1)]
zero_degree = set([i for i in range(1, n+1)])


# 그래프 생성
graph = {}
for i in range(1, n+1):
    graph[i] = []
# 간선 입력
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1
    zero_degree.discard(b)

while zero_degree:
    node = zero_degree.pop()
    print(node, end=' ')

    # 자식노드의 진입차수 감소 및 zero_degree 업데이트
    for node2 in graph[node]:
        indegree[node2] -= 1
        if indegree[node2] == 0:
            zero_degree.add(node2)