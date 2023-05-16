n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

white = 0
blue = 0

def checkAndCut(x_start, y_start, n):
    global white, blue
    
    check = True    # True: 더 자르지 않음
    # 전체가 같은 색인지 확인
    first_color = lst[y_start][x_start]
    for i in range(y_start, y_start+n):
        for j in range(x_start, x_start+n):
            if lst[i][j] != first_color:
                check = False
    if check:
        if first_color == 0:
            white += 1
        else:
            blue += 1
    else:
        subSize = n//2
        checkAndCut(x_start, y_start, subSize)
        checkAndCut(x_start, y_start+subSize, subSize)
        checkAndCut(x_start+subSize, y_start, subSize)
        checkAndCut(x_start+subSize, y_start+subSize, subSize)
        
        
checkAndCut(0, 0, n)

print(white)
print(blue)