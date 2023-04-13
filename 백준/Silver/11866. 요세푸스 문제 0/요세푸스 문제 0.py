import sys, collections

deq = collections.deque()
list = []

n, k = map(int, sys.stdin.readline().split())

for i in range(1, n+1):
    deq.append(i)

cnt = 0
while True:
    cnt += 1
    try:
        if cnt % k == 0:
            list.append(deq.popleft())
        else:
            deq.append(deq.popleft())
    except:
        break
    
print('<%d' %list.pop(0), end='')
for i in list:
    print(',', i, end="")
print('>')
