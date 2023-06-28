n = int(input())

board = []
houses = set()
for i in range(n):
    board.append([])
    for j, house in enumerate(input()):
        if house == '1':
            houses.add((i, j))
        board[-1].append(int(house))

nums = []
    
while houses:
    s = houses.pop()
    houses.add(s)
    stack = [s]
    searched = set([s])
    num = 0
    while stack:
        num += 1
        i, j = stack.pop()
        houses.remove((i, j))

        if i < n-1 and board[i+1][j] == 1 and (i+1, j) not in searched:
            stack.append((i+1, j))
            searched.add((i+1, j))
        if i > 0 and board[i-1][j] == 1 and (i-1, j) not in searched:
            stack.append((i-1, j))
            searched.add((i-1, j))
        if j < n-1 and board[i][j+1] == 1 and (i, j+1) not in searched:
            stack.append((i, j+1))
            searched.add((i, j+1))
        if j > 0 and board[i][j-1] == 1 and (i, j-1) not in searched:
            stack.append((i, j-1))
            searched.add((i, j-1))
            
    nums.append(num)

nums.sort()

print(len(nums))
for i in nums:
    print(i)