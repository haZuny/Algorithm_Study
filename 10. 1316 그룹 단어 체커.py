import sys

list = []
n = int(sys.stdin.readline())
for i in range(n):
    list.append(sys.stdin.readline())

groupWordNum = 0

for word in list:
    lastCharacter = ''
    flag = True
    checked = []
    for c in word:
        if c in checked and c != lastCharacter:
            flag = False
            break
        else:
            checked.append(c)
            lastCharacter = c
    if(flag):
        groupWordNum += 1
print(groupWordNum)
