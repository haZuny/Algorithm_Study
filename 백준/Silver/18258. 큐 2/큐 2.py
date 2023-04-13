import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    cmd = sys.stdin.readline()[:-1]
    if len(cmd) > 5:
        queue.appendleft(cmd.split()[1])
    else:
        if cmd == "pop":
            try:
                print(queue.pop())
            except:
                print(-1)
        elif cmd == "size":
            print(len(queue))
        elif cmd == "empty":
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif cmd == "front":
            try:
                print(queue[-1])
            except:
                print(-1)
        else:
            try:
                print(queue[0])
            except:
                print(-1)
