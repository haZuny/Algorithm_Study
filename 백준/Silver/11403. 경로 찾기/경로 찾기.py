n = int(input())

graph = {}
for i in range(n):
    graph[i] = []
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            graph[i].append(j)

for i in range(n):
    arr = [0 for j in range(n)]

    stack = []
    searched = []

    for node in graph[i]:
        stack.append(node)
        searched.append(node)

    while stack:
        current = stack.pop()
        arr[current] = 1
        for node in graph[current]:
            if node not in searched:
                stack.append(node)
                searched.append(node)

    print(' '.join(list(map(str, arr))))
