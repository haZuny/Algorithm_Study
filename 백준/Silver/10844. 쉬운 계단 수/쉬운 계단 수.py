n = int(input())

cnt = [0,1,1,1,1,1,1,1,1,1]

for _ in range(2, n+1):
    for i in range(10):
        temp = cnt[i]
        if i == 0:
            cnt[i] = cnt[i+1]
        elif i == 9:
            cnt[i] = before_i
        else:
            cnt[i] = before_i + cnt[i+1]
        before_i = temp
            
print(sum(cnt)%1000000000)
