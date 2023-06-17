n, m = map(int, input().split())
campus = []
for i in range(n):
    campus.append([])
    for j, c in enumerate(input()):
        campus[-1].append(c)
        if c == 'I':
            start = (i, j)
    
stack = [start]
searched = set([start])
cnt = 0


while stack:
    ci, cj = stack.pop()
    if campus[ci][cj] == 'P':
        cnt += 1
    if ci > 0 and campus[ci-1][cj] != 'X' and (ci-1, cj) not in searched:
        stack.append((ci-1, cj))
        searched.add((ci-1, cj))
    if ci < n-1 and campus[ci+1][cj] != 'X' and (ci+1, cj) not in searched:
        stack.append((ci+1, cj))
        searched.add((ci+1, cj))
    if cj > 0 and campus[ci][cj-1] != 'X' and (ci, cj-1) not in searched:
        stack.append((ci, cj-1))
        searched.add((ci, cj-1))
    if cj < m-1 and campus[ci][cj+1] != 'X' and (ci, cj+1) not in searched:
        stack.append((ci, cj+1))
        searched.add((ci, cj+1))

if cnt == 0:
    print('TT')
else:
    print(cnt)
