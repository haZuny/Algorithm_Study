n, m = map(int, input().split())

s = []

def select(last):
    if len(s) >= m:
        print(" ".join(map(str, s)))
        
    else:
        for i in range(last+1, n+1):
            #if not i in s:
            s.append(i)
            select(i)
            s.pop()

select(0)
