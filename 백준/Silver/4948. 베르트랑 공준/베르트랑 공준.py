import sys, math

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    count = 0
    for i in range(n+1, 2*n+1):
        if i < 2:
            continue
        
        sosu = True
        for j in range(2, int(math.sqrt(i)+1)):
            if i % j == 0:
                sosu = False
                break
            
        if sosu:
            count += 1
            
    print(count)
