import sys

dict = {i:0 for i in range(1, 10001)}

n = int(sys.stdin.readline())
for _ in range(n):
    dict[int(sys.stdin.readline())]+=1
for i in range(1,10001):
    if dict[i]!=0:
        for _ in range(dict[i]):
            print(i)

