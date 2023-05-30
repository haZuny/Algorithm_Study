'''
     n
n-1 n+1 2*n
형태로 그래프가 있다고 가정
bfs로 탐색
'''
import collections
n, k = map(int, input().split())

queue = collections.deque()
queue.append((n, 0))
searched = set([n])

# bfs로 k가 나올 때 까지 탐색
while True:
    n, time = queue.popleft()
    searched.add(n)

    if n == k:
        print(time)
        break
    
    if (not n*2 in searched) and n != 0 and n < k:
        queue.append((n*2, time+1))
        
    if (not n+1 in searched) and n < k:
        queue.append((n+1, time+1))
        
    if (not n-1 in searched) and n > 0:
        queue.append((n-1, time+1))
