# mbti 거리 구하는 함
def getDistance(m1, m2):
    distance = 0
    for i in range(4):
        if m1[i] != m2[i]:
            distance += 1
    return distance

# mbti 카운트
def getMbtiIdx(mbti):
    idx = 0
    if mbti[0] == 'E': idx += 8
    if mbti[1] == 'S': idx += 4
    if mbti[2] == 'F': idx += 2
    if mbti[3] == 'J': idx += 1
    return idx

t = int(input())
for _ in range(t):
    n = int(input())
    # mbti 유형별로 3개씩만 받음
    mbtiCnt = [0] * 16
    mbtis = []
    for mbti in input().split():
        idx = getMbtiIdx(mbti)
        if mbtiCnt[idx] < 3:
            mbtis.append(mbti)
            mbtiCnt[idx] += 1
            
    n = len(mbtis)

    # 최소값 탐색
    minDist = float('inf')

    # 브루트포스 탐색
    i, j, k = 0, 1, 2

    if n == 1:
        minDist = 0
    elif n == 2:
        minDist = getDistance(mbtis[0], mbtis[1])

    while i <= n-3:
        # 거리 계산
        dist = getDistance(mbtis[i], mbtis[j]) + getDistance(mbtis[k], mbtis[j]) + getDistance(mbtis[i], mbtis[k])

        # 최소값 선택
        minDist = min(minDist, dist)

        # 다음 인덱스 탐색
        k += 1
        if k > n-1:
            j += 1
            k = j+1
        if j > n-2:
            i += 1
            j = i+1
            k = j+1
            
    print(minDist)
