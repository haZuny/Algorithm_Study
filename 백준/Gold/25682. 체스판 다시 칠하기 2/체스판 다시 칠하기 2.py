import sys

n, m, k = map(int, input().split())

board_B = [[0 for _ in range(m+1)] for _ in range(n+1)]
board_W = [[0 for _ in range(m+1)] for _ in range(n+1)]

minVal = float("inf")

for i in range(1, n+1):
    row_B = [0 for _ in range(m+1)]
    row_W = [0 for _ in range(m+1)]
    
    for j, state in enumerate(sys.stdin.readline()[:-1]):
        j += 1

        # 누적합 계산
        row_B[j] = row_B[j-1]
        row_W[j] = row_W[j-1]
        board_B[i][j] = board_B[i-1][j] + row_B[j]
        board_W[i][j] = board_W[i-1][j] + row_W[j]
            
        # 현재 상태 반영
        if (i-j) % 2 == 0:  # 시작 색 차례          
            # 오류, 블랙 시작 케이스
            if state == 'W':
                board_B[i][j] += 1
                row_B[j] += 1
            # 오류, 화이트 시작 케이스
            else:
                board_W[i][j] += 1
                row_W[j] += 1        
        else:   # 시작 반대 색 차례
            # 오류, 화이트 시작 케이스
            if state == 'W':
                board_W[i][j] += 1
                row_W[j] += 1
            # 오류, 블랙 시작 케이스
            else:
                board_B[i][j] += 1
                row_B[j] += 1

        # 최소값 탐색
        if i >= k and j >= k:
            valB = board_B[i][j] - board_B[i-k][j] - board_B[i][j-k] + board_B[i-k][j-k]
            valW = board_W[i][j] - board_W[i-k][j] - board_W[i][j-k] + board_W[i-k][j-k]

            if valB < minVal:
                minVal = valB
            if valW < minVal:
                minVal = valW
                
print(minVal)