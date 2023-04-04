import sys

t = int(sys.stdin.readline())

money = [25, 10, 5, 1]
arr = []

for i in range(t):
    arr.append([])

    c = int(sys.stdin.readline())
    for mon in money:
        num = c // mon
        c = c % mon
        arr[i].append(num)

for moneys in arr:
    for coin in moneys:
        print(coin, end=' ')
    print()
    
