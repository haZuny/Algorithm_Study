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
for i in range(m-n+1):
    if sn == s[i:i+n]:
        cnt += 1

print(cnt)
