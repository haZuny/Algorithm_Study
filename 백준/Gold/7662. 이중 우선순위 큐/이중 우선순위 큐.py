import collections, heapq, sys


t = int(sys.stdin.readline())

for _ in range(t):
    # 입력 및 초기화
    q = int(sys.stdin.readline())

    cnt = 0
    maxHeap = []
    minHeap = []
    id = 0
    nums = set()
    
    for _ in range(q):
        command, n = input().split()
        n = int(n)
        
        # push
        if command == 'I':
            heapq.heappush(maxHeap, (-n, id))
            heapq.heappush(minHeap, (n, id))
            nums.add(id)
            id +=1; cnt+= 1

        # pop max
        elif n == 1:
            v = None
            while maxHeap:
                v, k = heapq.heappop(maxHeap)
                v *= -1
                if k in nums:
                    break
                else:
                    v = None
            if v != None:
                cnt -= 1
                nums.remove(k)

        # pop min
        else:
            v = None
            while minHeap:
                v, k = heapq.heappop(minHeap)
                if k in nums:
                    break
                else:
                    v = None
            if v != None:
                cnt -= 1
                nums.remove(k)

    # 출력1
    maxv = None
    while maxHeap:
        maxv, k = heapq.heappop(maxHeap)
        maxv *= -1
        if k in nums:
            break
        else:
            maxv = None
    if maxv != None:
        cnt -= 1
        nums.remove(k)

    # 출력2
    minv = None
    while minHeap:
        minv, k = heapq.heappop(minHeap)
        if k in nums:
            break
        else:
            minv = None
    if minv != None:
        cnt -= 1
        nums.remove(k)

    # 0개, 1개 남은 경우 처리, 출력
    if maxv == None:
        print('EMPTY')
    else:
        if minv == None:
            minv = maxv
        print(maxv, minv)



