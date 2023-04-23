n = int(input())
lst = [(int(input()),)]    #[(한칸오른경우, 두칸오른경우)]
for _ in range(n-1):
    n = int(input())
    try:    # 두번째 계단
        ifSeq = lst[-1][1] + n
    except:
        ifSeq = lst[-1][0] + n
    try:    # 두번째 계단
        ifNotSeq = max(lst[-2]) + n
    except:
        ifNotSeq = n
    lst.append((ifSeq, ifNotSeq))
print(max(lst[-1]))
