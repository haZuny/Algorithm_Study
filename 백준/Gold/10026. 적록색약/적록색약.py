n = int(input())
arr =[]
arr2 = []
for _ in range(n):
    arr.append(input())
    temp = ''
    for c in arr[-1]:
        temp += 'B' if c == 'B' else 'R'
    arr2.append(temp)

# 일반 사람
unsearchedPos = set()
for i in range(n):
    for j in range(n):
        unsearchedPos.add((i, j))
ans_normal = 0
# dfs 탐색하며 구역의 수 구함
while unsearchedPos:
    ans_normal += 1
    start = unsearchedPos.pop()
    unsearchedPos.add(start)
    color = arr[start[0]][start[1]]
    stack = [start]
    searched = set([start])
    while stack:
        current = stack.pop()
        unsearchedPos.remove(current)
        i, j = current
        if i < n-1 and arr[i+1][j] == color and (i+1, j) not in searched:
            stack.append((i+1, j))
            searched.add((i+1, j))
        if i > 0 and arr[i-1][j] == color and (i-1, j) not in searched:
            stack.append((i-1, j))
            searched.add((i-1, j))
        if j < n-1 and arr[i][j+1] == color and (i, j+1) not in searched:
            stack.append((i, j+1))
            searched.add((i, j+1))
        if j > 0 and arr[i][j-1] == color and (i, j-1) not in searched:
            stack.append((i, j-1))
            searched.add((i, j-1))

# 적록색약
unsearchedPos = set()
for i in range(n):
    for j in range(n):
        unsearchedPos.add((i, j))
ans_rg = 0
# dfs 탐색하며 구역의 수 구함
while unsearchedPos:
    ans_rg += 1
    start = unsearchedPos.pop()
    unsearchedPos.add(start)
    color = arr2[start[0]][start[1]]
    stack = [start]
    searched = set([start])
    while stack:
        current = stack.pop()
        unsearchedPos.remove(current)
        i, j = current
        if i < n-1 and arr2[i+1][j] == color and (i+1, j) not in searched:
            stack.append((i+1, j))
            searched.add((i+1, j))
        if i > 0 and arr2[i-1][j] == color and (i-1, j) not in searched:
            stack.append((i-1, j))
            searched.add((i-1, j))
        if j < n-1 and arr2[i][j+1] == color and (i, j+1) not in searched:
            stack.append((i, j+1))
            searched.add((i, j+1))
        if j > 0 and arr2[i][j-1] == color and (i, j-1) not in searched:
            stack.append((i, j-1))
            searched.add((i, j-1))

print(ans_normal, ans_rg)