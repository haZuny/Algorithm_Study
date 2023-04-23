n = int(input())
ls = [0, 0, 1, 1]
for i in range(4, n+1):
    remain = i%3
    case3 = ls[i//3] + remain
    remain = i%2
    case2 = ls[i//2] + remain
    case1 = ls[i-1]
    ls.append(min(case3, case2, case1)+1)
print(ls[n])
