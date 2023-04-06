'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
'''

import sys

n = int(sys.stdin.readline())
print(n * (n+1) * (n-4) // 6 + n)    # 코드 1 수행 횟수
print(3)    # 코드 1 O(n)
