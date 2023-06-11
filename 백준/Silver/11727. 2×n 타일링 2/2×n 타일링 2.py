n = int(input())

ans = 0

fac = [0, 1]

def getFac(n):
    if n >= len(fac):
        for i in range(len(fac), n+2):
            fac.append(fac[-1]*i)
        return fac[-1]
    else:
        return fac[n]

ans = 0

for i in range(n//2+1):
    num_2_1 = n - i*2
    try:
        ans += (2**i) * (getFac(i+num_2_1) // (getFac(i) * getFac(num_2_1)))
    except:
        ans += 2**i

print(ans%10007)