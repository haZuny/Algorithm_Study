n, m = map(int, input().split())
lst = [0]
cntLst = [0]*m
cnt = 0
fac = 1
for i in map(int, input().split()):
    lst.append((lst[-1]+i)%m)
    if lst[-1] == 0:
        cntLst[0] += fac
        fac += 1
    else:
        cnt += cntLst[lst[-1]]
        cntLst[lst[-1]] += 1

print(cnt + cntLst[0])
