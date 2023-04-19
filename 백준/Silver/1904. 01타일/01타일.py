n = int(input())

# f(n) = f(n-1) + f(n-2)

arr = [1,2]

for i in range(2,n):
    arr.append((arr[i-1] + arr[i-2])%15746)

print(arr[n-1])
        
