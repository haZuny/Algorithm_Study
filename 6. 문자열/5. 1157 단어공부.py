import sys

s = sys.stdin.readline()[:-1]

ls = []
for i in range(26):
    ls.append(0)

a_ASCII = ord('a')
A_ASCII = ord('A')

for i in range(len(s)):
    c = s[i]
    for j in range(26):
        if ord(c) == a_ASCII + j or ord(c) == A_ASCII + j:
            ls[j] += 1

maxIdx = 0
for i in range(26):
    if ls[i] > ls[maxIdx]:
        maxIdx = i
max = ls[maxIdx]

if ls.count(max) >= 2:
    print('?')
else:
    print(chr(A_ASCII + maxIdx))
