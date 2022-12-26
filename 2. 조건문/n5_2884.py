h, m = map(int, input().split())

all = ((24*60) + 60*h+m - 45)%(24*60)
h = all // 60
m = all % 60
print(str(h) + " " + str(m))
