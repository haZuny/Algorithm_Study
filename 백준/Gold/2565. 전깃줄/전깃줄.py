'''
1. 1차원 리스트 형태로 전깃줄 모양 저장
2. 모든 부분이 증가 혹은 감소 수열이여야지 안꼬임
3. 최대 증가 수열 길이 구함
4. 전체 길이에서 마이너스
'''

n = int(input())

temp = [-1 for _ in range(500)]
arr = []
dp_inc = [1 for _ in range(n)]    # 증가 수열
dp_dec = [1 for _ in range(n)]    # 감소 수열

# 전기줄 순서대로 리스트에 저장
for i in range(n):
    a, b = map(int, input().split())
    temp[a-1] = b
for i in temp:
    if i != -1:
        arr.append(i)

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j]+1)
        else:
            dp_dec[i] = max(dp_dec[i], dp_dec[j]+1)
            
#print(n - max(dp_inc + dp_dec))
print(n-max(dp_inc))