import sys

list = []
list2 = []
for i in range(10):
    list.append(int(sys.stdin.readline()))

for i in list:
    if not i%42 in list2:
        list2.append(i%42)
print(len(list2))