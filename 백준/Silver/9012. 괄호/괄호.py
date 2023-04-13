import sys

t = int(sys.stdin.readline())

for _ in range(t):
    str = sys.stdin.readline()[:-1]
    stack = []
    yn = "YES"
    for s in str:
        if s == '(':
            stack.append(0)
        else:
            try:
                stack.pop()
            except:
                yn = "NO"
                break
    if len(stack) > 0:
        yn = "NO"
    print(yn)
