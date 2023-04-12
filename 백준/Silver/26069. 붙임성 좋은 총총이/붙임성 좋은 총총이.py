import sys

n = int(sys.stdin.readline())
danceSet = set()

for _ in range(n):
    s1, s2 = sys.stdin.readline().split()
    if s1 == "ChongChong" or s2 == "ChongChong":
        danceSet.add(s1)
        danceSet.add(s2)
    elif s1 in danceSet or s2 in danceSet:
        danceSet.add(s1)
        danceSet.add(s2)
        
print(len(danceSet))
