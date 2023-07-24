# BFS를 사용해서 풀이

import collections

def funcD(n):
    return (n*2)%10000

def funcS(n):
    return 9999 if n == 0 else n-1

def funcL(n):
    str_n = str(n)
    str_n = '0' * (4 - len(str_n)) + str_n
    rotate = str_n[1:] + str_n[0]
    return int(rotate)

def funcR(n):
    str_n = str(n)
    str_n = '0' * (4 - len(str_n)) + str_n
    rotate = str_n[3] + str_n[:3]
    return int(rotate)


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    queue = collections.deque()
    searched = set()

    # num, route
    queue.append((a, ''))
    searched.add(a)

    # bfs
    while queue:
        current, route = queue.popleft()

        if current == b:
            print(route)
            break

        pass_d = funcD(current)
        pass_s = funcS(current)
        pass_l = funcL(current)
        pass_r = funcR(current)

        if pass_d not in searched:
            queue.append((pass_d, route+'D'))
            searched.add(pass_d)
        if pass_s not in searched:
            queue.append((pass_s, route+'S'))
            searched.add(pass_s)
        if pass_l not in searched:
            queue.append((pass_l, route+'L'))
            searched.add(pass_l)
        if pass_r not in searched:
            queue.append((pass_r, route+'R'))
            searched.add(pass_r)
