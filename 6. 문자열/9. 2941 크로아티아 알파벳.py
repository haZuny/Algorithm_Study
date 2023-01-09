import sys

s = sys.stdin.readline()[:-1]


croatiaNum = 0

# dj= 검사
i = 0
while i < len(s)-2:
    if s[i] + s[i+1] + s[i+2] == 'dz=':
        croatiaNum += 1
        s = s[:i] + ' ' + s[i+3:]
        i -=2
    i += 1
        
# 두글자 검사
i = 0
croatiaList = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
while i < len(s)-1:
    if s[i] + s[i+1] in croatiaList:
        croatiaNum += 1
        s = s[:i] + ' ' + s[i+2:]
        i -=1
    i += 1

s = s.replace(" ", "")
print(croatiaNum + len(s))
