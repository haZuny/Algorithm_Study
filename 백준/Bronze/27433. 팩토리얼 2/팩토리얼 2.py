def getFac(n):
    if n == 0:
        return 1
    else:
        return n*getFac(n-1)

print(getFac(int(input())))
