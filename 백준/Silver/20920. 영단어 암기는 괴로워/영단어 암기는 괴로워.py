import sys

n, m = map(int, sys.stdin.readline().split())

# 개수 딕셔너리
wordDic = {}

for _ in range(n):
    word = sys.stdin.readline()[:-1]

    # 길이 미달 패스
    if len(word) < m:
        continue
    # 딕셔너리에 입력
    if word in wordDic:
        wordDic[word] += 1
    else:
        wordDic[word] = 1

# 정렬 순서 반환 함수
def sortPoint(word):
    return [-1*wordDic[word], -1*len(word), word]

sorted(wordDic, key=sortPoint)

dic = sorted(wordDic, key=sortPoint)
for i in dic:
    print(i)
