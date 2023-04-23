n = int(input())
lst = [list(map(int, input().split()))]
for _ in range(n-1):
    r,g,b = map(int, input().split())
    lst.append((min(lst[-1][1], lst[-1][2]) + r,
                min(lst[-1][0], lst[-1][2]) + g,
                min(lst[-1][0],lst[-1][1]) + b, ))
print(min(lst[-1][0], lst[-1][1], lst[-1][2]))
