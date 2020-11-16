#플로이드와샬은 모든 노드간의 최단거리를 전부 구하는 방식.
#바로가는 경로와 특정 지역을 경유해서 가는 경우 중 최소값으로 최신화 하면 됨

#이 문제는 같은 경로인데 소요시간은 다른 여려개의 노선이 주어질 수 있다. 이를 처리하는 코드가 있어야 함.
n = int(input())
m = int(input())

MAX = int(1e9)

graph = [[MAX] * n for _ in range(n)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    #경로를 입력 받을때 문제의 조건에 맞게 동일 경로라도 최소거리로 최신화하여 받는다.
    if cost < graph[start-1][end-1]:
        graph[start-1][end-1] = cost

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for i in range(n):
    for j in range(n):
        if graph[i][j] >= MAX:
            graph[i][j] = 0
        graph[i][j] = str(graph[i][j])

for i in range(n):
    print(" ".join(graph[i]))


