'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;

    case 5
    
    1 => 2 => 3,4,5
         3 => 4,5
         4 => 5
         
    2 => 3 => 4, 5
         4 => 5
         
    3 => 4 => 5
}
'''

import sys

n = int(sys.stdin.readline())

sum = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        sum += n - (j+1)
            

print(sum)    # 코드 1 수행 횟수
print(3)    # 코드 1 O(n)
