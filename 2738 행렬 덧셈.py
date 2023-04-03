import sys

n, m = map(int, sys.stdin.readline().split())
arr1 = []
for _ in range(n):
    arr1.append(list(map(int, sys.stdin.readline().split())))
arr2 = []
for _ in range(n):
    arr2.append(list(map(int, sys.stdin.readline().split())))

arr_new = []
for i in range(n):
    arr_new.append([])
    for j in range(m):
        arr_new[i].append(arr1[i][j] + arr2[i][j])

print(arr_new)
for ls1 in arr_new:
    for num in ls1:
        print(num, end=' ')
    print()
