t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = {}
    # 배추의 위치 그래프에 추가
    for _ in range(k):
        x, y = map(int, input().split())
        graph[(x, y)] = []
        # 사방향 노드 존재하는지 검사, 존재하면 연결
        if (x-1, y) in graph:
            graph[(x, y)].append((x-1, y))
            graph[(x-1, y)].append((x, y))
        if (x-1, y+1) in graph:
            graph[(x, y)].append((x-1, y+1))
            graph[(x-1, y+1)].append((x, y))
        if (x, y-1) in graph:
            graph[(x, y)].append((x, y-1))
            graph[(x, y-1)].append((x, y))
        if (x, y+1) in graph:
            graph[(x, y)].append((x, y+1))
            graph[(x, y+1)].append((x, y))

    cnt = 0
    # DFS로 각 그래프 탐색, 그래프의 개수 구하기
    while len(graph) > 0:
        #print(graph, end = '\n\n')
        # 첫 노드 삽입
        cnt += 1
        current = list(graph.keys())[0]
        visited = [current]
        stack = []
        for node in graph.pop(current):
            stack.append(node)
        # 스택의 요소 탐색
        while len(stack)>0:
            current = stack.pop()
            if not current in visited:
                visited.append(current)
                for node in graph.pop(current):
                    stack.append(node)
    print(cnt)