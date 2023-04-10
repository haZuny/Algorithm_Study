import sys

s = sys.stdin.readline().strip()
n = len(s)

s_set = set()
for i in range(n):  # i: 체크할 문자 길이
    for j in range(n-i+1):  # j: 체크 시작 지점
        s_set.add(s[j:j+i])

print(len(s_set))
