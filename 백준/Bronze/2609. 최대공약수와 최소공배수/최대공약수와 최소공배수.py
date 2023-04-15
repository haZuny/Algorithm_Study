n, m = map(int, input().split())

measure = 1

div = 2
while div <= n and div <= m:
    if n % div == 0 and m % div == 0:
        measure *= div
        n //= div
        m //= div
    else:
        div += 1
print(measure)
print(measure * n * m)
