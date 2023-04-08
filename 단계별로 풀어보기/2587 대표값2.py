import sys

ls = []
sum = 0

for _ in range(5):
    num = int(sys.stdin.readline())
    sum += num
    ls.append(num)

ls.sort()

print(sum // 5)
print(ls[2])
