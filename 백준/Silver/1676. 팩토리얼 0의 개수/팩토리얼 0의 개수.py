n = int(input())
fac = 1
for i in range(1, n+1):
    fac *= i

fac = str(fac)
cnt = 0
while fac[-1] == '0':
    cnt += 1
    fac = fac[:-1]

print(cnt)
