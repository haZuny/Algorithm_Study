all = int(input())
n = int(input())

testAll = 0
for i in range(n):
    price, num = map(int, input().split())
    testAll += price * num

if(testAll == all):
    print("Yes")
else:
    print('No')