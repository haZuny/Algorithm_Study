import sys

n = int(sys.stdin.readline())

answer = 0
addingNum = 6
lastNum = 1
while True:
    lastNum += 6 * answer
    if n <= lastNum:
        break
    else:
        answer += 1
        
print(answer+1)
#1
#2 ~ 7      6
#8 ~ 19     12
#20 ~ 37    18
#38 ~ 61    24

