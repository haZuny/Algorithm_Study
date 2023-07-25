import sys

n = int(sys.stdin.readline())

tree = {}

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    try:
        tree[a].append(b)
    except:
        tree[a] = [b]
    try:
        tree[b].append(a)
    except:
        tree[b] = [a]

parents = [-1 for _ in range(n+1)]

# dfs
stack = [(1, -1)]
searched = set([1])

while stack:
    current, parent = stack.pop()
    parents[current] = parent

    for i in tree[current]:
        if i not in searched:
            stack.append((i, current))
            searched.add(i)

for i in parents[2:]:
    print(i)
