'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;

    case 7
    1 2 3 4 5
      2 3 4 5 6
        3 4 5 6 7

        7 6 5
        3 2 1
'''

import sys

n = int(sys.stdin.readline())
print(n * (n-1) * (n-2) // 6)    # 코드 1 수행 횟수
print(3)    # 코드 1 O(n)
