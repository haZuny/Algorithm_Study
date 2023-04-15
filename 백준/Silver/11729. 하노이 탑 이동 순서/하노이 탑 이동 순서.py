ls = []
def hanoi(height, start, target, mid):
    if height > 1:
        hanoi(height-1, start, mid, target)
        ls.append(start)
        ls.append(target)
        hanoi(height-1, mid, target, start)
    else:
        ls.append(start)
        ls.append(target)

n = int(input())
hanoi(n, 1, 3, 2)
print(len(ls)//2)
for i in range(0, len(ls), 2):
    print(ls[i], ls[i+1])
    
