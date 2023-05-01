input()
s = input()

ascA = ord('a')
hash = 0

for i in range(len(s)):
    hash += (ord(s[i]) - ascA+1) * 31**i

print(hash)
