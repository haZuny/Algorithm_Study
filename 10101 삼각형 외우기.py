import sys

p1 = int(sys.stdin.readline())
p2 = int(sys.stdin.readline())
p3 = int(sys.stdin.readline())

if p1 + p2 + p3 == 180:
    if p1 == 60 and p2 == 60 and p3 == 60:
        print("Equilateral")
    elif p1 == p2 or p2 == p3 or p3 == p1:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print('Error')
