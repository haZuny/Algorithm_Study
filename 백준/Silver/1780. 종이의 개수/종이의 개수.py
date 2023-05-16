n = int(input())

# 입력
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

# 각 종이 갯수
cnt1 = 0
cnt2 = 0
cnt3 = 0


def divSearch(si, sj, n):
    global cnt1, cnt2, cnt3
    
    # 압축 가능한지 체크
    check = True    # True: 압축 가능
    firstColor = lst[si][sj]
    for i in range(si, si+n):
        for j in range(sj, sj+n):
            if lst[i][j] != firstColor:
                check=False
                break
        if not check:
            break

    if check:
        if firstColor == -1:
            cnt1 += 1
        elif firstColor == 0:
            cnt2 += 1
        else:
            cnt3 += 1
    
    else:
        ssize = n//3
        divSearch(si, sj, ssize)
        divSearch(si, sj+ssize, ssize)
        divSearch(si, sj+ssize*2, ssize)

        divSearch(si+ssize, sj, ssize)
        divSearch(si+ssize, sj+ssize, ssize)
        divSearch(si+ssize, sj+ssize*2, ssize)

        divSearch(si+ssize*2, sj, ssize)
        divSearch(si+ssize*2, sj+ssize, ssize)
        divSearch(si+ssize*2, sj+ssize*2, ssize)

divSearch(0,0,n)

print(cnt1)
print(cnt2)
print(cnt3)   