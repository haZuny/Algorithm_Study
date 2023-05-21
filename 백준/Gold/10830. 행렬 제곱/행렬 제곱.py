# int로 전환하고 1000 모듈러
def prepare(n):
    return int(n)%1000

n, b = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(prepare, input().split())))

# 행렬곱
def multi(l1, l2):
    lst = []
    for row in l1:
        rowTemp = []
        for i in range(n):  # l2 column idx
            temp = 0
            
            for j in range(n):  # l2 row idx
                temp += row[j] * l2[j][i]
            rowTemp.append(temp%1000)
        lst.append(rowTemp)
    return(lst)

# 분할 정복
def divConc(lst, b):
    if b == 1:
        return lst
    
    temp = divConc(lst, b//2)
    if b % 2 == 1:
        return multi(lst, multi(temp, temp))
    return multi(temp, temp)

# 출력
ans = divConc(lst, b)
for row in ans:
    print(" ".join(map(str, row)))
