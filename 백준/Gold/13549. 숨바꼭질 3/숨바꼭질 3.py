import collections

n, k = map(int, input().split())

queue = collections.deque([(n, 0)])
searched = set([n])

while True:
    current, cnt = queue.popleft()

    if current == k:
        print(cnt);break;
    else:
        if current*2 not in searched and current*2<=100000:
            queue.append((current*2, cnt))
            searched.add(current*2)
        if current-1 not in searched and current-1 >=0:
            queue.append((current-1, cnt+1))
            searched.add(current-1)
        if current+1 not in searched and current+1<=100000:
            queue.append((current+1, cnt+1))
            searched.add(current+1)
        
