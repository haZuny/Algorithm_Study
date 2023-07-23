'''
1 힙 두개를 사용해서 풀이
2 push연산에서 min heap, max heap 두개 모두 각각 삽입
3 push된 num은 nums에 기록
4 pop 연산시 두개 힙에서 각각 pop
5 만약 두 힙에 각각 값이 하나씩 남으면 dict에서 출력
'''
import collections, heapq, sys

nums = {}
cnt = 0
maxHeap = []
minHeap = []

# delete dict
def deleteNum(n):
    global nums

    nums[n] -= 1
    if nums[n] == 0:
        nums.pop(n)
    
# heap push
def heapPush(n):
    global cnt
    
    heapq.heappush(maxHeap, -1 * n)
    heapq.heappush(minHeap, n)

    try:
        nums[n] += 1
    except:
        nums[n] = 1
    cnt += 1
    

# heap pop
def heapPop(isMax):
    global cnt

    if cnt == 0:
        return None
    
    elif cnt == 1:
        while True:
            v = heapq.heappop(minHeap)
            if v in nums:
                break
        cnt -= 1
        deleteNum(v)
        return v
            
    else:
        if isMax:
            while True:
                v = -1 * heapq.heappop(maxHeap)
                if v in nums:
                    break
        else:
            while True:
                v = heapq.heappop(minHeap)
                if v in nums:
                    break
        cnt -= 1
        deleteNum(v)
        return v
        
t = int(sys.stdin.readline())

for _ in range(t):
    # 입력 및 초기화
    q = int(sys.stdin.readline())

    nums = {}
    cnt = 0
    maxHeap = []
    minHeap = []
    
    for _ in range(q):
        command, n = input().split()
        n = int(n)
        if command == 'I':
            heapPush(n)
        elif n == 1:
            heapPop(True)
        else:
            heapPop(False)


    maxV = heapPop(True)
    minV = heapPop(False)
    
    if maxV == None:
        print('EMPTY')
    else:
        if minV == None:
            minV = maxV
        print(maxV, minV)
    

