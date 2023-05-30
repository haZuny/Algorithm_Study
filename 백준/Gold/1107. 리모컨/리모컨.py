n = int(input())
m = int(input())
btns = [0,1,2,3,4,5,6,7,8,9]
if m > 0:
    for i in map(int, input().split()):
        btns.remove(i)

gotoNum = ''
minMove = 100 - n if 100 >= n else n - 100
lenTarget = len(str(n))

# 백트래킹으로 탐색
def bt(size):
    global gotoNum, minMove

    # 현재 위치에서 + 또는 -로 이동할 경우 횟수 계산
    if len(gotoNum) >= lenTarget-1 and len(gotoNum)>=1:
        curPos = int(gotoNum)
        move = size + curPos - n if curPos >= n else size + n - curPos
        if move < minMove:
            minMove = move

    # 길이가 타겟+1보다 길면 종료
    if len(gotoNum) >= lenTarget+1:
        return
        
    # 백트래킹
    for i in btns:
        gotoNum += str(i)
        bt(size+1)
        gotoNum = gotoNum[:-1]

bt(0)

print(minMove)
