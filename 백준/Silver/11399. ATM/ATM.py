n = int(input())
lst = list(map(int, input().split()))
lst.sort()

ans = 0
sum = 0

for i in lst:
    sum += i
    ans += sum

print(ans)
