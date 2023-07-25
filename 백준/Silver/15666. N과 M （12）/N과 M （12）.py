import sys

n, m = map(int, sys.stdin.readline().split())

filter = set(list(map(int, sys.stdin.readline().split())))

lst = sorted(list(filter))

def bt(stack, last_idx):
    global m, lst
    
    if len(stack) == m:
        print(' '.join(list(map(str, stack))))
        return

    for i, v in enumerate(lst[last_idx:]):
        bt(stack+[v], last_idx+i)

bt([], 0)


