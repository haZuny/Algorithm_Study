import sys, math

# 약수의 개수가 홀수 -> 열림, 짝수 -> 닫힘
# 약수의 개수가 홀수: 제곱수
# ==> n이하의 제곱수의 개수

n = int(sys.stdin.readline())

print(int(math.sqrt(n)))
