#위상정렬
#노드 방향성에 거스르지 않고록 순서대로 나열하는 것

#진입차수가 0인 노드를 큐에 넣는다
#큐가 빌 때까지
#   큐에서 원소를 꺼낸 뒤 해당 노드에서 출발하는 간선을 제거
#   새롭게 진입차수가 0이 된 애들을 큐에 넣는다.

#사이클이 있으면 안됨. 보통 문제에서 사이클이 발생하지 않는 경우만을 제시한다.

from collections import deque

#노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
indegree = [0] * (v + 1) #모든 노드에 대한 진입차수 0으로 초기화

#간선정보 저장을 위한 연결리스트 초기화
graph = [[] for i in range(v + 1)]

#간선정보 입력 받기
for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)  #a에서 b로 이동 가능함을 표시
    indegree[b] += 1    #진입차수 추가

def topology_sort():
    result = []
    q = deque()

    #진입차수가 0인 노드를 큐에 추가
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        #해당 원소와 연결된 노드들의 진입차수에서 1 씩 빼기
        for i in graph[now]:
            indegree[i] -= 1
            #새로 진입차수가 0이 되면 큐에 넣기
            if indegree[i] == 0:
                q.append(i)
    return print(result)

topology_sort()
