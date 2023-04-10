import sys

n = int(sys.stdin.readline())
peopleSet = set()
for _ in range(n):
    name, log = sys.stdin.readline().split()
    if log == 'enter':
        peopleSet.add(name)
    else:
        peopleSet.remove(name)

list = list(peopleSet)
list.sort(reverse=True)
for name in list:
    print(name)
