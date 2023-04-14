# 배열 뒤집을때 덱의 인풋, 아웃풋 방향 바꾸기
import sys, collections

t = int(sys.stdin.readline())

for _ in range(t):
    p = input()
    n = int(sys.stdin.readline())
    
    if n > 0:
        deq = collections.deque(list(map(int, sys.stdin.readline()[1:-2].split(','))))
    else:
        input()
        deq = collections.deque()
        
    popLeft = True
    err = False

    for func in p:
        if func == 'R':
            popLeft = not popLeft
        else:
            try:
                if popLeft:
                    deq.popleft()
                else:
                    deq.pop()
            except:
                err = True
                break
                
    if err:
        print('error')
    else:
        if not popLeft:
            deq.reverse()
        try:
            print('[%d' %deq.popleft(), end='')
            for i in range(len(deq)):
                print(",%d" %deq.popleft(), end='')
            print(']')
        except:
            print('[]')
            

    
