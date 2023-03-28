import sys
strList = []
for i in range(100):
    try:
        strList.append(sys.stdin.readline())
    except:
        break
for s in strList:
        if s != '\n':
            print(s, end='')
