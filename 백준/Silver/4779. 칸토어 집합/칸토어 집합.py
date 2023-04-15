def kanto(list, l, r):
    div3 = (r-l+1) // 3
    if r-l > 2:
        kanto(list, l, l + div3)
        kanto(list, l + div3*2, r)
        
    for i in range(l+div3, l+div3*2):
        list[i] = ' '
        
while True:
    try:
        n = int(input())
    except:
        break
    
    list = ['-' for _ in range(3**n)]
    kanto(list, 0, 3**n-1)

    for c in list:
        print(c, end='')
    print()
