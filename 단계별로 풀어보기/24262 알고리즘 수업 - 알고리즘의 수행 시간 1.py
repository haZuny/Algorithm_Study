import sys
import math

numState = 1
numList = []
stack = []
stackLog = []

# 스택 연산 함수
def push():
    global numState
    stack.append(numState)
    numState += 1
    stackLog.append('+')
def pop():
    stack.pop(-1)
    stackLog.append('-')
        

# 입력
n = int(sys.stdin.readline())
for i in range(n):
    numList.append(int(sys.stdin.readline()))

# 동작
while len(numList) != 0:
    num = numList[0]
    # 스택 비어있으면 push
    if len(stack) == 0:
        if numState <= num:
            push()
        else:
            break
        
    # 스택의 최상단 < num
    elif stack[-1] < num:
        if numState <= num:
            push()
        else:
            break
        
    # 스택의 최상단 == num
    elif stack[-1] == num:
        pop()
        numList.pop(0)
        
    # 스택의 최상단 > num
    else:
        break

if len(stackLog) < n * 2:
    print('NO')
else:
    for i in stackLog:
        print(i)
