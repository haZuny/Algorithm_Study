def dn(a):
    sum = a
    for i in str(a):
        sum += int(i)
    return sum
    

list = list(range(1,10001))

for i in range(10001):
    d = dn(i)
    if d in list:
        list.remove(d)

for i in list:
    print(i)
