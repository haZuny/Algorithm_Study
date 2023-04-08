import sys

num = int(sys.stdin.readline())

n = num // 4
str = "int"

str = 'long ' * n + str
print(str)
