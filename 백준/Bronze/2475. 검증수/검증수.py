sum = 0
for i in input().split():
    i = int(i)
    sum += i ** 2

print(sum%10)
