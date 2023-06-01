'''
n = 1+n-1 or 2+n-2 + 3+n-3
f(n) = f(n-1)*a + f(n-2)*b + f(n-3)*c

1 1
2 2
3 4
4 7
5 13
6 24
7 44
=> fib를 이전 3개 더하는 것
'''
# dp 배열 3까지 초기화
fib3 = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0]

# 최대 탐색 위치
searched = 3

t = int(input())
for _ in range(t):
    n = int(input())
    if n <= searched:
        print(fib3[n])
    else:
        for i in range(searched+1, n+1):
            fib3[i] = fib3[i-1]+fib3[i-2]+fib3[i-3]
        
        print(fib3[n])
        searched = n          
