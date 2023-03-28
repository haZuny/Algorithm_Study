import sys
'''
case 1 3
1 3 6
1 2 3

case 3 5
1 6 21 56
1 5 15 35   56
1 4 10 20   35
1 3 6 10    20
1 2 3 4     10

case 3 3
1 5 15  21
1 4 10  15
1 3 6   10
1 2 3   6

case 3 2
1 5     6
1 4     5
1 3     4
1 2     3

case 1 1    
1   1
1   1

case 3 1
1
1
1
'''

t = int(sys.stdin.readline())
for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    list = [[]]
    for ni in range(1, n+1):
        list[0].append(ni)
        
    for ki in range(1, k+1):
        list.append([1])
        
        
        for ni in range(1, n):
            list[ki].append(list[ki][ni-1] + list[ki-1][ni])
    print(list[ki][n-1])
    
