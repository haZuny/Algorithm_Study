n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

all = set([i for i in range(n)])
teamA = []

minSub = n ** n * 100

# 팀 탐색, n//2개 뽑는 모든 경우
def getTeam(n, m, last):
    global minSub
    
    if len(teamA) == m:
        teamB = list(all - set(teamA))
        pointTeamA = 0
        pointTeamB = 0
        for i in range(m):
            for j in range(i+1, m):
                pointTeamA += s[teamA[i]][teamA[j]] + s[teamA[j]][teamA[i]]
                pointTeamB += s[teamB[i]][teamB[j]] + s[teamB[j]][teamB[i]]
        sub = pointTeamA - pointTeamB
        if sub < 0: sub *= -1
        if sub < minSub: minSub = sub
                
    else:
        for i in range(0, n):
            if i > last:
                teamA.append(i)
                getTeam(n, m, i)
                teamA.pop()

getTeam(n, n//2, 0)
print(minSub)
