import sys

def check(a):
    str_a = str(a)
    for i in range(1, len(str_a) - 1):
        if int(str_a[i-1]) - int(str_a[i]) != int(str_a[i]) - int(str_a[i+1]):
            return False
    return True

n = int(sys.stdin.readline())
cnt = 0
for i in range(1, n+1):
    if(check(i)):
        cnt += 1
print(cnt)
