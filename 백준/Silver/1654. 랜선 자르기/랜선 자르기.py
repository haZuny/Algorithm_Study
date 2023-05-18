k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

# 만들 수 있는지 검사
def check(length):
    cnt = 0
    for line in lines:
        cnt += line//length
    if cnt >= n:
        return True
    return False

left = 1
right = max(lines)

while right-left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

if check(right):
    print(right)
else:
    print(left)
