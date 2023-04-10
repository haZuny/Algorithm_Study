import sys

n, m = map(int, sys.stdin.readline().split())

list = []
dic = {}
for i in range(n):
    word = sys.stdin.readline().strip()
    list.append(word)
    dic[word] = i+1

for _ in range(m):
    word = sys.stdin.readline().strip()
    if word[0] >= 'A' and word[0] <='Z':
        print(dic[word])
    else:
        print(list[int(word)-1])
