import sys

m, n = map(int, sys.stdin.readline().split())

list = []
for _ in range(m):
    list.append(sys.stdin.readline().strip())

minCount = 64

# 각 8*8 사이즈 모두 검사
for i in range(m - 7):
    for j in range(n - 7):
        count = 0
        
        start = 'W'

        # 각 칸 검사
        for ii in range(i, i+8):
            # 가장 첫번째줄 컬러
            if ii % 2 == i % 2:
                start_row = start
            else:
                start_row = 'W' if start == 'B' else 'B'

            for jj in range(j, j+8):
                if jj % 2 == j % 2:
                    if list[ii][jj] != start_row:
                        count += 1
                else:
                    if list[ii][jj] == start_row:
                        count += 1

        if count < minCount:
            minCount = count

        count = 0
        start = 'B'

        # 각 칸 검사
        for ii in range(i, i+8):
            # 가장 첫번째줄 컬러
            if ii % 2 == i % 2:
                start_row = start
            else:
                start_row = 'W' if start == 'B' else 'B'

            for jj in range(j, j+8):
                if jj % 2 == j % 2:
                    if list[ii][jj] != start_row:
                        count += 1
                else:
                    if list[ii][jj] == start_row:
                        count += 1

        if count < minCount:
            minCount = count
            
print(minCount)
