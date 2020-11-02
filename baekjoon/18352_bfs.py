#길 최단거리문제는 bfs로 접근해야한다.
from _collections import deque
n, m, k, start = map(int,input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1) #최단거리 리스트.
distance[start] = 0

q = deque()
q.append(start)
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1: #거리가 계산되지 않은곳은 방문한적이 없던 곳.
            distance[next_node] = distance[now] + 1 # 단방향에서 bfs로 한번 방문되면 다른곳을 경유하는 경우는 없다.
            q.append(next_node)

results = []
for i in range(n+1):
    if distance[i] == k:
        results.append(i)

if results:
    results.sort()
    for i in results:
        print(i)
else:
    print(-1)


#dfs로 풀려했던 코드. 방문처리를 하지 않아서 테스트케이스는 돌아가지만 채점에선 런타임 에러가 났다.
# 거리가 같은 최단거리 문제는 bfs로 접근하자.
# def dfs(start, shortest, current_dist):
#     shortest[start] = min(shortest[start], current_dist)
#
#     for next_node in graph[start]:
#         dfs(next_node, shortest, current_dist + 1)
#
#
# dfs(start, shortest, 0)
#
# results = []
# for i in range(1,n+1):
#     if shortest[i] == k:
#         results.append(i)
#
# if not results:
#     print(-1)
# else:
#     for i in results:
#         print(i)



