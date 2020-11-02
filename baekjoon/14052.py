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
def dfs(graph,x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if ny >= 0 and nx >= 0 and nx < n and ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                dfs(graph, nx, ny)

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
    global origin_graph
    #벽을 다 세웠으면 바이러스 퍼뜨리고 계산

    if walls == 0:
        walled_graph = copy.deepcopy(origin_graph)

        for i in range(n):
            for j in range(m):
                if walled_graph[i][j] == 2:
                    dfs(walled_graph, i, j)

        result = max(result, cal_safezone(walled_graph))
        return result

    for i in range(n):
        for j in range(m):
            if origin_graph[i][j] == 0:
                origin_graph[i][j] = 1
                origin_graph(walls - 1)
                origin_graph[i][j] = 0

print(dfs_wall(3))
