lst = list(map(int, input().split()))

up = True
down = True
last = lst[0]

for i in lst[1:]:
    if i > last:
        down = False
    else:
        up = False
    last = i

if up:
    print('ascending')
elif down:
    print('descending')
else:
    print('mixed')
