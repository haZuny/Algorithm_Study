n, m = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()

def bt(stack, lst, m):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    try:
        last = stack[-1]
    except:
        last = 0

    for i in lst:
        if i >= last:
            bt(stack+[i], lst, m)
            
bt([], ls, m)
