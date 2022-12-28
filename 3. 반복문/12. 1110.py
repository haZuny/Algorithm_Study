import sys

num = int(sys.stdin.readline())
changed = num
cycle = 0

while True:
    changed = 10 * (changed % 10) + (changed // 10 + changed % 10) % 10
    cycle += 1

    # 비교
    if changed == num:
        break

print(cycle)