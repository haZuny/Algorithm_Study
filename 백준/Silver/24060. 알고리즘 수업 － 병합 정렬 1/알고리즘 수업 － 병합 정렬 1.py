def merge(list, p, q, r):
    global cnt, k
    
    i = p
    j = q + 1
    temp = []
    while i <= q and j <= r:
        if list[i] <= list[j]:
            temp.append(list[i])
            i += 1
        else:
            temp.append(list[j])
            j += 1
    while i <= q:
        temp.append(list[i])
        i += 1
    while j <= r:
        temp.append(list[j])
        j += 1

    i = p
    t = 0
    while i <= r:
        cnt += 1
        if cnt == k:
            print(temp[t])
        list[i] = temp[t]
        i += 1
        t += 1

def merge_sort(list, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(list, p, q)
        merge_sort(list, q+1, r)
        merge(list, p, q, r)

n, k = map(int, input().split())
cnt = 0
list = list(map(int, input().split()))
merge_sort(list, 0, len(list)-1)
if cnt < k:
    print(-1)
    
