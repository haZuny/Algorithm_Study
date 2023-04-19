n = int(input())
cnt = 0
chess = []

def bt(size):
    global cnt
    
    if size == n:
        cnt += 1
        #print(chess)
        return

    canPut = [i for i in range(n)]
    for i in range(size):
        try:
            canPut.remove(chess[i])
        except:
            pass
        try:
            canPut.remove(chess[i]+size-i)
        except:
            pass
        try:
            canPut.remove(chess[i]+i-size)
        except:
            pass

    for i in canPut:
        
        chess.append(i)
        bt(size + 1)
        chess.pop()
        
bt(0)
print(cnt)
