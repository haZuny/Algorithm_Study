t = int(input())
for _ in range(t):
    n = int(input())
    dict = {}
    for _ in range(n):
        cloth, category = input().split()
        try:
            dict[category] += 1
        except:
            dict[category] = 1
    ans = 1
    for key in dict:
        ans *= (dict[key]+1)
    print(ans-1)