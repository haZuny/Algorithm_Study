import sys

word = sys.stdin.readline()[:-1]

lenWord = len(word)
flag = 1

while lenWord > 1:
    if word[0] == word[-1]:
        word = word[1:-1]
        lenWord -= 2
    else:
        flag = 0
        break

print(flag)
