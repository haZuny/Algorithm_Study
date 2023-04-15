str = input()
for c in str:
    if ord(c) >= ord('a'):
        print(chr(ord(c) - 32), end='')
    else:
        print(chr(ord(c) + 32), end='')
