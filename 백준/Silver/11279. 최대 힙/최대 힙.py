import heapq, sys

heap = []

n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, -x)