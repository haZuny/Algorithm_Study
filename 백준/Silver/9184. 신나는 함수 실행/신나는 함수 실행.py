w = [[[1 for k in range(21)] for j in range(21)] for i in range(21)]

for i in range(1,21):
        for j in range(1,21):
            for k in range(1,21):
                if i < j and j < k:
                    w[i][j][k] = w[i][j][k-1] + w[i][j-1][k-1] - w[i][j-1][k]
                else:
                    w[i][j][k] = w[i-1][j][k] + w[i-1][j-1][k] + w[i-1][j][k-1] - w[i-1][j-1][k-1]
                    

while True:
    a,b,c = map(int, input().split())
    
    if a == -1 and b == -1 and c == -1:
        break
    
    print(f"w({a}, {b}, {c}) = ", end="")
    
    if a <= 0 or b <= 0 or c <= 0:
        print(1)
        continue
    
    if a > 20 or b > 20 or c > 20:
        a = 20
        b = 20
        c = 20

    print(w[a][b][c])
