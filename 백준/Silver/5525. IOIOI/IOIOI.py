n = int(input())
m = int(input())
s = input()

n = 2*n + 1

sn = ''
for i in range(n):
    if i%2 == 0:
        sn+='I'
    else:
        sn += 'O'
    
cnt = 0

sc = s[0]
bc = s[0]
num = 1
for i in range(1, m):
    # 연속해서 다른 문자 나올 때
    if s[i] != bc:
        num += 1
    # 연속 깨질 때
    else:
        if sc == 'O':
            num -= 1
        if s[i-1] == 'O':
            num -= 1
        if num >= n:
            cnt += 1
            num -= n
            cnt += num//2
        sc = s[i]
        num = 1
    bc = s[i]


if sc == 'O':
    num -= 1
if s[-1] == 'O':
    num -= 1
if num >= n:
    cnt += 1
    num -= n
    cnt += num//2

print(cnt)