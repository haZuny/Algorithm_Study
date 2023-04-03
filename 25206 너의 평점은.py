import sys

allSum = 0
num = 0

for _ in range(20):
    name, point, grade = sys.stdin.readline().split()
    point = float(point)
    # P나 아니면 합산
    if grade != 'P':
        num += point

    if grade == 'A+':
        allSum += 4.5 * point
    elif grade == 'A0':
        allSum += 4.0 * point
    elif grade == 'B+':
        allSum += 3.5 * point
    elif grade == 'B0':
        allSum += 3.0 * point
    elif grade == 'C+':
        allSum += 2.5 * point
    elif grade == 'C0':
        allSum += 2.0 * point
    elif grade == 'D+':
        allSum += 1.5 * point
    elif grade == 'D0':
        allSum += 1.0 * point
    elif grade == 'F':
        allSum += 0 * point

print(allSum / num)
