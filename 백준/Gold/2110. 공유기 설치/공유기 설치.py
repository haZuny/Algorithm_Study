n, c = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(int(input()))
lst.sort()

def check(gap):
    cnt = 1
    last = lst[0]
    for pos in lst[1:]:
        if pos-last >= gap:
            cnt += 1
            last = pos
    if cnt >= c:
        return True
    else:
        return False

s = 0
e = 1000000000

while e-s > 1:
    mid = (s+e)//2
    if check(mid):
        s = mid
    else:
        e = mid

if check(e):
    print(e)
else:
    print(s)
