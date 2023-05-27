'''
fn+2 = [1 1] [fn+1]
             [fn]
             
fn+1 = [1 0] [fn+1]
             [fn]

==>

[fn+2  = [1 1] [fn+1]
 fn+1]   [1 0] [fn]

==>

Un+1 = A Un

U1 = [1] #f2
     [0] #f1
U2 = A U1
U3 = A A U1
'''
# 초기 행렬
matU1 = [[1], [0]]
matA = [[1,1],[1,0]]

# 행렬곱
def multiMat(arr1, arr2):
    '''
        1
        2
    1 2
    3 4
    5 6
    '''
    res = []
    for i in range(len(arr1)):  # arr1의 row
        res.append([])
        for j in range(len(arr2[0])):  # arr2의 column
            temp = 0
            for k in range(len(arr1[0])):  # arr2의 row, arr1의 column
                temp += (arr1[i][k] * arr2[k][j])
            res[i].append(temp%1000000007)
    return res
        

# 분할정복으로 An을 구함
def getA(n):
    if n == 1:
        return matA
    elif n % 2 == 0:
        temp = getA(n//2)
        return multiMat(temp, temp)
    else:
        temp = getA(n//2)
        return multiMat(matA, multiMat(temp, temp))

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(1)
elif n == 3:
    print(2)
else:
    powerA = getA(n-1)
    matUn = multiMat(powerA, matU1)
    print(matUn[0][0])