n = int(input())

# 입력
img = []
for _ in range(n):
    img.append(list(map(int, list(input()))))

def zip(si, sj, n):
    # 압축 가능한지 체크
    check = True    # True: 압축 가능
    firstColor = img[si][sj]
    for i in range(si, si+n):
        for j in range(sj, sj+n):
            if img[i][j] != firstColor:
                check=False
                break
        if not check:
            break

    if check:
        return str(firstColor)
    else:
        nextSize = n//2
        ans = '(' + zip(si, sj, nextSize)+\
            zip(si, sj+nextSize, nextSize)+\
            zip(si+nextSize, sj, nextSize)+\
            zip(si+nextSize, sj+nextSize, nextSize)+')'
        return ans
    
print(zip(0,0,n))