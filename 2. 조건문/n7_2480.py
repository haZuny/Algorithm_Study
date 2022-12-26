n1, n2, n3 = map(int, input().split())

# 모두 같은 경우
if n1 == n2 and n1 == n3:
    money = 10000 + n1*1000
# 두개만 같은 경우
elif n1 == n2:
    money = 1000 + n1 * 100
elif n3 == n2:
    money = 1000 + n2 * 100
elif n1 == n3:
    money = 1000 + n1 * 100
# 모두 다른 경우
else:
    if n1 > n2 and n1 > n3:
        money = n1 * 100
    elif n2 > n1 and n2 > n3:
        money = n2 * 100
    else:
        money = n3 * 100

print(money)