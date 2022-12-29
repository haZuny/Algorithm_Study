import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))

print('%d %d'%(min(list), max(list)))