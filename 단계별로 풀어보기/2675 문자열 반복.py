import sys

n = int(sys.stdin.readline())
testCase = []
for i in range(n):
    testCase.append(sys.stdin.readline()[:-1])

for case in testCase:
    n, s = case.split()
    n = int(n)
    new = ''
    for c in s:
        new += c * n
    print(new)

