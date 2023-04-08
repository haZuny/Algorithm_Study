import sys

while True:
    l1, l2, l3 = map(int, sys.stdin.readline().split())

    # 종료 판별
    if l1 == 0 and l2 == 0 and l3 == 0:
        break

    # 삼각형 조건 판별
    if max(l1, l2, l3) < l1 + l2 + l3 - max(l1, l2, l3):
        if l1 == l2 and l2 == l3:
            print("Equilateral")
        elif l1 == l2 or l2 == l3 or l3 == l1:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")
    
