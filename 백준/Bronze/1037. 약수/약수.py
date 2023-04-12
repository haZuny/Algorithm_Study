import sys

sys.stdin.readline()
dic = {}
maxNum = 1
for num in list(map(int, sys.stdin.readline().split())):
    if num > maxNum:
        maxNum = num
        
    cnt = 0
    div = 2
    while div <= num:
        if num % div == 0:
            cnt += 1
            num //= div
        else:
            try:
                if dic[div] < cnt:
                    dic[div] = cnt
            except:
                if cnt != 0:
                    dic[div] = cnt
            cnt = 0
            div += 1
        try:
            if dic[div] < cnt:
                dic[div] = cnt
        except:
            if cnt != 0:
                dic[div] = cnt

answer = 1
for i in dic:
    answer *= (i**dic[i])
    
if answer == maxNum:
    print(answer * min(dic))
else:
    print(answer)
