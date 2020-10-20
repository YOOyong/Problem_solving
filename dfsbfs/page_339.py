# 그래프에서 간선의 비용이 모두 동일 할 때는
# bfs로 최단 거리를 찾을 수 있다.
from collections import deque

n, m, k, x = map(int,input().split())
graph= [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()

    for next in graph[now]:
        if distance[next] == -1: #아직 가지 않은곳이다
            distance[next] = distance[now] + 1
            q.append(next)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)








