import collections

n, k = map(int, input().split())
deq = collections.deque()

for _ in range(n):
    deq.appendleft(int(input()))

cnt = 0

for coin in deq:
    cnt += k//coin
    k %= coin
    if k == 0:
        break

print(cnt)