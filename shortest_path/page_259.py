n, m = map(int, input().split())
INF = int(1e9)

#그래프 초기화
graph = [[INF] * (n+1) for _ in range((n+1))]

#자기 자신에게 가는 경우 0으로
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

#연결 노드 입력받고 거리 업데이트
for _ in range(m):
    start, to = map(int,input().split())
    graph[start][to] = 1
    graph[to][start] = 1

finish, visit = map(int,input().split())

#floid
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#k를 거쳐 a에서 x로 가는 최단소요시간.
answer =  graph[1][visit] + graph[visit][finish]

if answer >= INF:
    print(-1)
else:
    print(answer)