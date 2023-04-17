n, m = map(int, input().split())

s = []

def select():
    if len(s) >= m:
        print(" ".join(map(str, s)))
        
    else:
        for i in range(1, n+1):
            if not i in s:
                s.append(i)
                select()
                s.pop()

select()
