#탐색으로 조합을 구하는 법을 익혀야 한다.
import copy
n, m = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

origin_graph = []
for _ in range(n):
    origin_graph.append(list(map(int, input().split())))

result = 0

#바이러스 dfs
#함수로 받은 그래프에서 계산을 진행.
#먼저 복사되어 있어야함?
def dfs(graph,x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if ny >= 0 and nx >= 0 and nx < n and ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                dfs(graph, nx, ny)

#그래프의 세이프 존 확인
#주어진 그래프는 벽이 세워지고 난 뒤의 그래프여야 한다.
def cal_safezone(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count

#벽을 치는 dfs
def dfs_wall(walls):
    global result
    #벽을 다 세웠으면 바이러스 퍼뜨리고 계산
    if walls == 0:
        walled_graph = copy.deepcopy(origin_graph)

        for i in range(n):
            for j in range(m):
                if walled_graph[i][j] == 2:
                    dfs(walled_graph, i, j)

        result = max(result, cal_safezone(walled_graph))
        return

    for i in range(n):
        for j in range(m):
            if origin_graph[i][j] == 0: #벽이 없는곳이면
                origin_graph[i][j] = 1 # 벽을 친다.
                dfs_wall(walls - 1)# 세번이 될 때까지 벽을 친다.
                origin_graph[i][j] = 0 # 위 재귀가 끝나면 세웠던 벽을 없앤다.


dfs_wall(3)
print(result)
