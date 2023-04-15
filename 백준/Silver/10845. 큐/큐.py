import collections, sys

queue = collections.deque()

n = int(input())
for _ in range(n):
    s = sys.stdin.readline()[:-1]
    if len(s) >= 6:
        x = int(s.split()[1])
        queue.append(x)
    elif s == 'pop':
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif s == 'size':
        print(len(queue))
    elif s == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif s == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    else:
        try:
            print(queue[-1])
        except:
            print(-1)
