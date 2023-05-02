n, k = map(int, input().split())

sumLst = [0]
for i in map(int, input().split()):
    sumLst.append(sumLst[-1] + i)

seqLst = []

for i in range(k, n+1):
    seqLst.append(sumLst[i] - sumLst[i-k])
    
print(max(seqLst))
