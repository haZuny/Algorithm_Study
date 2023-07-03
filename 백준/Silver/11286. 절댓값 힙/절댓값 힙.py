import sys
import heapq

n = int(sys.stdin.readline())
heap = []
dict = {}   # 절대값이 같은 경우 작은수 출력 = 음수 출력, 음수 존재 여부 기록

for _ in range(n):
    x = int(sys.stdin.readline())

    # 출력 case
    if x == 0:
        try:
            v = heapq.heappop(heap)
            # 같은 절대값에 음수 존재할 경우, 음수 출력
            if -v in dict and dict[-v] > 0:
                print(-v)
                dict[-v] -= 1
            else:
                print(v)
        except:
            print(0)
    # push case(양수)
    elif x > 0:
        heapq.heappush(heap, x)
    # push case(음수)
    else:
        heapq.heappush(heap, -x)
        # 음수의 개수 카운트
        try:
            dict[x] += 1
        except:
            dict[x] = 1