'''
repeat xpos until xpos<max:
    xpos에서 가능한 y 개수 구하기
'''
def solution(k, d):
    answer = 0
    for xpos in range(0, d+1, k):
        answer += ((d**2 - xpos**2)**(1/2))//k + 1
    return answer