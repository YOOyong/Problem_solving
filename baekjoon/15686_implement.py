#궅이 매트릭스로 그리지 않아도
#좌표만 있으면 계산이 가능한 문제이다.
#매트릭스로 그릴지 좌표의 리스트만 만들지 시작할 때 고민해봐야 할 듯.
# 아래는 매트릭스를 만들어서 살짝 비효율적인것 같다.
from itertools import combinations
n, m = map(int, input().split())

graph = [[0] for _ in range(n+1)]

for i in range(n):
    graph[i+1].extend(list(map(int,input().split())))

chikenhomes = []
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == 2:
            chikenhomes.append((i, j))

selecteds = list(combinations(chikenhomes, m))

def chicken_dist(selected):
    result = 0
    for x in range(1,n+1):
        for y in range(1,n+1):
            if graph[x][y] == 1:
                temp = 1e9
                for cx, cy in selected:
                    temp = min(temp, abs(x - cx) + abs(y - cy))
                result += temp
    return result

answer = 1e9
for selected in selecteds:
    answer = min(answer, chicken_dist(selected))

print(answer)
