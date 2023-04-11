import sys, math

# 소수 구하는 함수
def checkSosu(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

t = int(sys.stdin.readline())
max = 2
sosuSet = set()

# 각 테스트 케이스 반복
for _ in range(t):
    n = int(sys.stdin.readline())

    count = 0
    sosu_list = set()

    # 소수 세트 구함
    if n > max:
        for i in range(max, n):
            if checkSosu(i):
                sosuSet.add(i)
        max = n

    # 파티션 검
    for i in range(2, n//2+1):
        if i in sosuSet and n-i in sosuSet:
            count += 1
            
    print(count)
    
