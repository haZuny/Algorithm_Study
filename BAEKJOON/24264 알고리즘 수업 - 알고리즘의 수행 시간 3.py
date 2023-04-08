'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
}
'''

import sys

n = int(sys.stdin.readline())

print(n)    # 코드 1 수행 횟수
print(1)    # 코드 1 O(n)
