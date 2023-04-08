n, k = map(int, input().split())

def getFac(a):
    res = 1
    for i in range(1, a+1):
        res = res * i % 1000000007
    return res


print((getFac(n) / getFac(n-k) / getFac(k)))