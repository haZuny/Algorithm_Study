n, m, b = map(int, input().split())

cntPerH = {}    # 각 높이별 개수
timePerH = {}    # 각 높이로 맞추는데 걸리는 시간
for _ in range(n):
    # 각 높이에 대한 개수 딕셔너리에 저장
    for i in map(int, input().split()):
        try:
            cntPerH[i] += 1
        except:
            cntPerH[i] = 1

# 높이를 targetH로 맞추는 경우 시간 탐색
for targetH in range(min(cntPerH)-1, max(cntPerH)+1):
    if targetH < 0:
        continue
    time = 0
    tempB = b
    # 각 높이별 처리 시간 체크
    for h in cntPerH:
        # 목표보다 높은 땅인 경우
        if h > targetH:
            tempB += cntPerH[h] * (h - targetH)
            time += cntPerH[h] * (h - targetH) * 2
        # 목표보다 낮은 땅인 경우
        elif h < targetH:
            tempB -= cntPerH[h] * (targetH - h)
            time += cntPerH[h] * (targetH - h)
            
    # 블럭이 남아있을 때만 기록
    if tempB >= 0:
        timePerH[targetH] = time

# 시간 딕셔너리 (value(오름), key(내림) 순으로 정렬)
sortedTime = sorted(timePerH, key = lambda x:(timePerH[x], -x))

# 출력
bestH = sortedTime[0]
print(timePerH[bestH], bestH)