import sys

n = int(sys.stdin.readline())
list1 = set(sys.stdin.readline().split())
m = int(sys.stdin.readline())
list2 = sys.stdin.readline().split()

for num in list2:
    if num in list1:
        print(1, end=' ')
    else:
        print(0, end=' ')
