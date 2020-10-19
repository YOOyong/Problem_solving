import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]
for _ in range(m):
     init, to, time = map(int, input().split())
     graph[init].append((to, time))

def dijkstra(start):
    q = []
    heapq.headpush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]: #현 노드에서 갈수 있는곳을 순회하며
            cost = dist + i[1] #다음 갈 수 있는 노드까지의 거리 계산
            if cost < distance[i[0]]: #계산된 거리가 원래 거리보다 더 작으면
                distance[i[0]] = cost #거리를 업데이트
                heapq.heappush(q, (cost, i[0])) # 노드까지의 최단거리를


dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF: # inf면 가는 경로가 없다는 뜻이다.
        count += 1
        max_distance = max(max_distance, d)

print(count-1 , max_distance)