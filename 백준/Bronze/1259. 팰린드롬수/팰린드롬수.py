def check(s):
    if len(s) <= 1:
        return 'yes'
    elif s[0] != s[-1]:
        return 'no'
    else:
        return check(s[1: -1])

while True:
    s = input()
    if s == '0':
        break
    print(check(s))

