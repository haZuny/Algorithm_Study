n = int(input())

def recursion(s):
    global cnt
    cnt += 1
    if len(s) <= 1:
        return 1
    elif s[0] != s[-1]:
        return 0
    else:
        return recursion(s[1:-1])

for _ in range(n):
    str = input()
    cnt = 0
    print(recursion(str), cnt)
