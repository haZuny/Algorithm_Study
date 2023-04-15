s = input()
point = 0.0
if len(s) == 2:
    if s[0] == 'A':
        point += 3.7
    elif s[0] == 'B':
        point += 2.7
    elif s[0] == 'C':
        point += 1.7
    else:
        point += 0.7

    if s[1] == '+':
        point += 0.6
    elif s[1] == '0':
        point += 0.3
print("%.1f"%point)
