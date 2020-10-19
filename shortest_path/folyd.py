INF = int(1e9)
#노드의 개수 n 간선의 개수 m
n = int(input())
m = int(input())

#2차원 리스트를 모두 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

#자기 자신에게 가는 비용은 0으로
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

#각 간선에 대한 정보 입력받기
for _ in range(m):
    start, to, cost = map(int, input().split())
    graph[start][to] = cost

#점화식에 따라 플로이드 워셜 수행
for k in range(1 , n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)