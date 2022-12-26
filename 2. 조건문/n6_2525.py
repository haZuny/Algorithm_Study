h, m = map(int, input().split())
addT = int(input())

all = (h*60 + m + addT) % (24 * 60)

h = all // 60
m = all % 60

print(str(h) + " " + str(m))