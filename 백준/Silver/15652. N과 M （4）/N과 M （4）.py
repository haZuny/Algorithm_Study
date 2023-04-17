n, m = map(int, input().split())

s = []

def select(last):
    if len(s) >= m:
        print(" ".join(map(str, s)))
        
    else:
        for i in range(last, n+1):
            s.append(i)
            select(i)
            s.pop()

select(1)

