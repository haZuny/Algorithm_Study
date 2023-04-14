import sys, collections

n,m = map(int, sys.stdin.readline().split())
deq = collections.deque()
for i in range(1, n+1):
    deq.append(i)

list = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in list:
    idx = deq.index(i)
    mid = len(deq)//2
    # 앞에 있던게 뒤로
    if idx <= mid:
        rotateNum = -1
        rotateCnt = idx
    # 뒤에 있던게 앞으로
    else:
        rotateNum = 1
        rotateCnt = len(deq)-idx
    # 값 찾을때까지 회전
    for j in range(rotateCnt):
        cnt += 1
        deq.rotate(rotateNum)
    deq.popleft()
print(cnt)
