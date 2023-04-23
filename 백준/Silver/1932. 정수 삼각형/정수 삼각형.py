n = int(input())
maxLst = [int(input())]
for i in range(n-1):
    temp = []
    idx = 0
    for n in map(int, input().split()):
        if idx == 0:
            temp.append(maxLst[idx]+n)
        elif idx== i+1:
            temp.append(maxLst[idx-1]+n)
        else:
            temp.append(max(maxLst[idx], maxLst[idx-1])+n)
        idx += 1
    maxLst = temp
print(max(maxLst))
