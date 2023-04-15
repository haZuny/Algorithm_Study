def getFibo(n):
    if n > 1:
        return getFibo(n-1) + getFibo(n-2)
    elif n == 1:
        return 1
    else:
        return 0

print(getFibo(int(input())))
