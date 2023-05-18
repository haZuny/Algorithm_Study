n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 해당 높이에서 나무를 얻을 수 있는지 체크
def check(h):
    sum = 0
    for tree in trees:
        if tree > h:
            sum += tree-h
    if sum >= m:
        return True
    return False

left = 0
right = 1000000000

while right-left > 1:
    mid = (left+right)//2
    
    if check(mid):
        left = mid
    else:
        right = mid

if check(left):
    print(left)
else:
    print(right)

 