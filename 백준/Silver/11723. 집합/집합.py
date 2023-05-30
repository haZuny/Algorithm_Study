import sys

m = int(sys.stdin.readline())
mySet = set()
for _ in range(m):
    s = sys.stdin.readline().split()
    if len(s) == 2:
        s[1] = int(s[1])
        
    if s[0] == 'add':
        mySet.add(s[1])
    elif s[0] == 'remove':
        try:
            mySet.remove(s[1])
        except:
            pass
    elif s[0] == 'check':
        print(1 if s[1] in mySet else 0)
    elif s[0] == 'toggle':
        if s[1] in mySet:
            mySet.remove(s[1])
        else:
            mySet.add(s[1])
    elif s[0] == 'all':
        mySet = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    else:
        mySet = set()