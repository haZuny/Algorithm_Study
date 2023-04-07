import sys

n = int(sys.stdin.readline())

check = 665
while n != 0:
    check += 1
    if '666' in str(check):
        n -= 1
    
print(check)
