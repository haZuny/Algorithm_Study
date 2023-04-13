import sys, collections


n = int(sys.stdin.readline())
deq = collections.deque()
for _ in range(n):
    
    cmd = sys.stdin.readline().split()

    if len(cmd) == 2:
        if cmd[0] == 'push_back':
            deq.append(cmd[1])
        else:
            deq.appendleft(cmd[1])
    elif cmd[0] == "pop_front":
        try:
            print(deq.popleft())
        except:
            print(-1)
    elif cmd[0] == "pop_back":
        try:
            print(deq.pop())
        except:
            print(-1)
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        if deq:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        try:
            print(deq[0])
        except:
            print(-1)
    else:
        try:
            print(deq[-1])
        except:
            print(-1)
