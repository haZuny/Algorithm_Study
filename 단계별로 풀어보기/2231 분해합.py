import sys

num = int(sys.stdin.readline())

answer = 0

for i in range(1, num+1):
    sum = i
    string_i = str(i)
    for n in string_i:
        sum += int(n)
    if sum == num:
        answer = i
        break
    
print(answer)
    
