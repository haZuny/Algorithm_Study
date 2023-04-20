t = int(input())
arr = [1,1,1]
max_i = 3

for _ in range(t):
    n = int(input())
    for i in range(max_i, n):
        arr.append(arr[i-2]+arr[i-3])
    if n > max_i:
        max_i = n
    print(arr[n-1])
