n = int(input())
lst = [(int(input()),)]    #[(한칸오른경우, 두칸오른경우)]
for _ in range(n-1):
    n = int(input())
    try:
        ifSeq = lst[-1][1] + n
    except:    # 두번째 계단 에러 방지
        ifSeq = lst[-1][0] + n
    try:
        ifNotSeq = max(lst[-2]) + n
    except:    # 두번째 계단 에러 방지
        ifNotSeq = n
    lst.append((ifSeq, ifNotSeq))
print(max(lst[-1]))
