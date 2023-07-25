a, b = map(int, input().split())

def bt(num, cnt):
    global b
    
    if num == b:
        print(cnt)
        exit()

    elif num > b:
        return

    else:
        bt(num*2, cnt+1)
        bt(num*10+1, cnt+1)

bt(a, 1)
print(-1)
