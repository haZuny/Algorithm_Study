import sys, math

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    if n < 2:
        n = 2

    while True:
        sosu = True
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                sosu = False
                break
        
        if sosu:
            print(n)
            break
        else:
            n += 1



    
