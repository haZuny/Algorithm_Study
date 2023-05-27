'''
fn = fn-1 + fn-2

0===
1
0
1
1
2
4
6


1===
0
1
1
2
.
.

'''
import sys

arr0 = [1, 0, 1]
arr1 = [0, 1, 1]
max = 2

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(input())
    if n > max:
        for i in range(max+1, n+1):
            arr0.append(arr0[i-1]+ arr0[i-2])
            arr1.append(arr1[i-1]+ arr1[i-2])
        max = n
    print(arr0[n], arr1[n])
