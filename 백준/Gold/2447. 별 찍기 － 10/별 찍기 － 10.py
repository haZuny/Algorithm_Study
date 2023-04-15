def draw(list, lx, ly, rx, ry, gab):
    
    if gab >= 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                draw(list, lx + gab * i, ly +gab * j, lx + gab * (i+1)-1, ly + gab * (j+1)-1, gab//3)
    
    for i in range(lx+gab, lx+gab*2):
        for j in range(ly+gab, ly+gab*2):
            list[i][j] = ' '

n = int(input())
list = [['*' for _ in range(n)] for _ in range(n)]

draw(list, 0, 0, n-1, n-1, n//3)

for i in range(n):
    for j in range(n):
        print(list[i][j], end='')
    print()
