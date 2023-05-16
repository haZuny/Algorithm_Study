exp = input().split('-')

first = exp[0].split('+')
exp = exp[1:]

ans = 0

for i in first:
    ans += int(i)

for i in exp:
    temp = 0
    for j in i.split('+'):
        temp += int(j)
    ans -= temp

print(ans)
