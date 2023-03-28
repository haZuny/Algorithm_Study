import sys

x = int(sys.stdin.readline())

# addNum: 커지는 수
addNum = 1
searching = 0

while True:
    if searching + addNum >= x:
        seq = x - searching
        if addNum % 2 == 0:
            print('%d/%d' %(seq, addNum + 1 - seq))
        else:
            print('%d/%d' %(addNum + 1 - seq, seq))
        break
    searching += addNum
    addNum += 1
    
