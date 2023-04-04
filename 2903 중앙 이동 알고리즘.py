import sys

n = int(sys.stdin.readline())

sidePoint = 1

# 양 끝을 제외한 한 변의 점의 수 구하기
for i in range(1, n):
    sidePoint = sidePoint * 2 + 1

# 전체 사각형 수
numSquare = (2**n)**2

# 중복 포함한 점의 수
allPoint = numSquare * 4

# 중복 제거 점의 수
    # 1. 각 변의 점은 2개의 사각형에 걸침
    # 2. 사각형 내부의 점은 4개의 사각형에 걸침
num = allPoint - sidePoint * 4 - (sidePoint**2*3)
print(num)
