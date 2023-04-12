import sys

added = 0
numList = []
numCntDic = {}
maxCntNum = 0

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    added += num
    numList.append(num)
    if num in numCntDic:
        numCntDic[num] += 1
    else:
        numCntDic[num] = 1
    #최고빈도 계산
    if maxCntNum < numCntDic[num]:
        maxCntNum = numCntDic[num]

numList.sort()
maxList = []
for i in numCntDic:
    if maxCntNum == numCntDic[i]:
        maxList.append(i)
maxList.sort()
cnt = len(numList)

print(round(added/cnt))
print(numList[cnt//2])
if len(maxList) >= 2 and numCntDic[maxList[0]] == numCntDic[maxList[1]]:
    print(maxList[1])
else:
    print(maxList[0])
print(numList[-1] - numList[0])
