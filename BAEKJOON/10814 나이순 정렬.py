import sys

n = int(sys.stdin.readline())

dic = {}

for _ in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    if age in dic:
        dic[age].append(name)
    else:
        dic[age] = [name]

for age in sorted(dic):
    for name in dic[age]:
        print(age, name)
