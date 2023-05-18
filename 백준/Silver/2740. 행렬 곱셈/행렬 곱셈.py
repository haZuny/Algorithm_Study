arrA = []
arrB = []

n, m = map(int, input().split())
for _ in range(n):
    arrA.append(list(map(int, input().split())))
    
k = int(input().split()[-1])
for _ in range(m):
    arrB.append(list(map(int, input().split())))
    
for row in arrA:
    for i in range(k):
        s = []
        for j in range(m):
            s.append(row[j] * arrB[j][i])
        print(sum(s), end=' ')
    print()