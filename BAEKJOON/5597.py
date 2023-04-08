import sys

list = []

for i in range(28):
    list.append(int(sys.stdin.readline()))

list2 = []

for i in range(1, 31, 2):
    f1 = False
    f2 = False
    for j in list:
        if i == j:
            f1 = True
        if i+1 == j:
            f2 = True
    if not f1:
        list2.append(i)
    if not f2:
        list2.append((i+1))
print(min(list2))
print(max(list2))