zeroPos = []
board = []
for i in range(9):
    board.append(list(map(int, input().split())))
    for j in range(9):
        if board[i][j] == 0:
            zeroPos.append((i,j))

def sdoku(idx):
    if idx == len(zeroPos):
        for row in board:
            print(" ".join(map(str, row)))
        exit()
        
    x = zeroPos[idx][0]
    y = zeroPos[idx][1]
    
    for i in range(1, 10):
        # 가로
        if i in [board[j][y] for j in range(9)]:
            continue
        # 세로
        if i in [board[x][j] for j in range(9)]:
            continue
        # 대각선
        isBreak = False
        for j in range(3):
            for k in range(3):
                if i == board[(x//3)*3+j][(y//3)*3+k]:
                    isBreak = True
        if isBreak:
            continue
                
        board[x][y] = i
        sdoku(idx+1)
        board[x][y] = 0
       
sdoku(0)