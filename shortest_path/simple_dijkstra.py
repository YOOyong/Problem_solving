import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)] # 각 노드에 연결된 노드에 대한 리스트
visited = [False] * (n+1) # 방문여부 리스트
distance = [INF] * (n + 1) #최단거리 inf로 초기화

#간선, 비용 입력받기
for _ in range(m):
    start, to, cost = map(int, input().split())
    graph[start].append((to, cost))

def get_smallest_node():

    min_value = INF
    index = 0 # 가장 최단거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0 #시작노드 거리 초기화
    visited[start] = True #시작노드 방문처리
    for j in graph[start]:  #시작노드에 연결된 노드마다
        distance[j[0]] = j[1]  #거리를 업데이트
    for i in range(n-1): #시작 노드를 제외한 모든 노드를 순회하며
        now = get_smallest_node() #현재에서 가장 거리가 짧은 노드를 선택
        visited[now] = True  #방문처리
        for j in graph[now]: #현노드에 연결된 노드마다
            cost = distance[now] + j[1] #비용 계산.
            if cost < distance[j[0]]:  #비용이 원래 비용보다 작으면
                distance[j[0]] = cost  #업데이트

dijkstra(start)

print(distance)
