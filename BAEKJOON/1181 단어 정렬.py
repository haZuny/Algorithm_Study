import sys

n = int(sys.stdin.readline())
dic = {}
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    word_size = len(word)
    if word_size in dic:
        dic[word_size].append(word)
    else:
        dic[word_size] = [word]

lastWord = ''
for size in sorted(dic):
    words = dic[size]
    words.sort()
    for word in words:
        if word != lastWord:
            print(word)
            lastWord = word
