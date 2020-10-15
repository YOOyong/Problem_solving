from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]



def bfs(x, y):
    q = deque()
    q.append((x,y)) #현위치 넣기

    while q: #큐가 빌 때 까지
        x, y = q.popleft()
        #현위치에서 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m: #벗어난 범위 무시
                continue
            if graph[nx][ny] == 0:                     #벽 무시
                continue

            if graph[nx][ny] == 1:  #안가본 곳일 경우
                graph[nx][ny] = graph[x][y] + 1 #노드까지의 거리를 업데이트
                q.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))


