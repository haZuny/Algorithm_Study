GROUP_1 = -1
GROUP_2 = -2

# 카드 번호 i를 파이썬의 인덱스화
getIdx = lambda num:num-1

# 주어진 번호를 열때의 그룹을 나눠서 탐색
def search(cards, num, group):
    board = cards.copy()
    groupCnt = 0
    # 오픈한 상자의 번호가, 그룹에 속하지 않을 때까지 탐색
    while board[getIdx(num)] not in (GROUP_1, GROUP_2) :
        groupCnt += 1
        temp = num
        num = board[getIdx(num)]
        board[getIdx(temp)] = group
    return (board, groupCnt)

def solution(cards):
    answer = 0
    
    size = len(cards)
    # 모든 경우의 수 탐색
    for i in range(1, size+1):
        cardsTemp, groupSize_1 = search(cards, i, GROUP_1)
        for j in range(1, size+1):
            ttt, groupSize_2 = search(cardsTemp, j, GROUP_2)
            # 점수가 최대값이면 answer 갱신
            if groupSize_1 * groupSize_2 > answer: answer = groupSize_1 * groupSize_2;
            
    return answer