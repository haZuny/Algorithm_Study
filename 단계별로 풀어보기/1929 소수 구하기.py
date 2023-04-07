'''
2 #### 3 5 7 ## 11 13 ## 17 19 ## 23 ## ## 29 31 33 ## 37 39 41 43 ## 47 ## 51 53 ##


마지막: 1 3 7 9
'''

import sys

m,n = map(int, sys.stdin.readline().split())

list = [i for i in range(3, n+1, 2)]

if m <= 2:
    print(2)

listSize = len(list)
i = 0
while i < len(list):
    val = list[i]
    if val >= m:
        print(val)
        
    j = i + 1
    while j < listSize:
        if list[j] % val ==0:
            list.pop(j)
            listSize -= 1
        else:
            j += 1
    
    i += 1

