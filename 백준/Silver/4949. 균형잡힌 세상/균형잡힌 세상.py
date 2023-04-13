import sys

while True:
    str = sys.stdin.readline()[:-1]
    if str == ".":
        break
    stack = []
    answer = "yes"
    for s in str:
        if s == '(':
            stack.append(0)
        elif s == '[':
            stack.append(1)
        elif s == ')':
            try:
                c = stack.pop()
                if c != 0:
                    answer = "no"
            except:
                answer = "no"
        elif s == ']':
            try:
                c = stack.pop()
                if c != 1:
                    answer = "no"
            except:
                answer = "no"
    if len(stack) > 0:
        answer = "no"
    print(answer)
