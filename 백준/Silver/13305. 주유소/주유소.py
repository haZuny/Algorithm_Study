n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
idx = 0
minIdx = 0
for i in range(n-1):
    if price[i] < price[minIdx]:
        minPrice = price[minIdx]
        for j in range(minIdx, i):
            ans += minPrice * length[j]
        minIdx = i
        
minPrice = price[minIdx]
for i in range(minIdx, n-1):
    ans += minPrice * length[i]

print(ans)
