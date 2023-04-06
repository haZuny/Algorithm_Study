import sys

n, b = sys.stdin.readline().split()
b = int(b)

# 최종 반환값
num_2 = 0
# 곱해지며 각 자리의 수를 계산할 
bb = 1

for i in range(len(n)-1, -1,-1):
    # 알파벳
    cnum = 0
    if n[i] >= 'A' and n[i] <= 'Z':
        cnum = ord(n[i]) - ord('A') + 10
    # 숫자
    else:
        cnum = int(n[i])

    num_2 += cnum * bb
    bb *= b

print(num_2)
