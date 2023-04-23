input()
lst = [-1001]
for n in map(int, input().split()):
    lst.append(max(n, n+lst[-1]))
print(max(lst))
