import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)] # 각 노드에 연결된 노드에 대한 리스트
distance = [INF] * (n + 1) #최단거리 inf로 초기화

#간선, 비용 입력받기
for _ in range(m):
    start, to, cost = map(int, input().split())
    graph[start].append((to, cost))

def dijkstra(start):
    q = []
    #시작 노드로 가기위한 최단경로는 0으로 설정, 큐에 넣기
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:# 큐가 비어있지 않으면
        #가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현 노드가 이미 처리된 적이 있다면 무시
        if distance[now] < dist:
            continue

        #현 노드와 연결된 다른 노드 탐색
        for i in graph[now]:
            cost = dist + i[1]
            #현 노드를 거쳐서 다른 노드로 가는 경우가 더 빠른 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

print(distance)

def test(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] #현 노드를 거쳐 다음 노드(i[0])로 가기 위한 비용
            if cost < distance[i[0]]: #그 비용이 다음 노드로 가는 원래 비용보다 작으면
                distance[i[0]] = cost #그 비용으로 업데이트하고
                heapq.heappush(q, (cost, i[0])) #힙에 추가.

#큐를 초기화하고 현노드를 거쳐가는 거리 0으로 현노드를q에 추가
#거리테이블 업데이트
#큐가 있는동안
#큐안에 있는 일정을 하나 뽑는다 큐에는 해당노드까지의 거리가 있음
#그 거리가 거리테이블에 있는 거리보다 크면 넘어간다.
#그게 아니라면
#해당 노드에서 갈 수 있는 노드들을 순회하며
#해당 노드까지의 거리 + 갈 수 있는 노드까지의 거리를 더함.
#위 계산 결과가 거리테이블에 있는 갈 수 있는 노드의 거리값보다 작으면 업데이트를 하고
#(업데이트된 거리, 갈 수있는 노드)를 힙에 업데이트