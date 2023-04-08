'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''

import sys

n = int(sys.stdin.readline())

sum = 0
for i in range(n):
    sum += i

print(sum)    # 코드 1 수행 횟수
print(2)    # 코드 1 O(n)
