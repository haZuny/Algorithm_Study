year = int(input())

isYoon = 0
if year % 4 == 0:
    isYoon = 1
    if year % 100 == 0:
        isYoon = 0
        if year % 400 == 0:
            isYoon = 1
print(isYoon)