#dfs 풀이
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

apt = 0
def dfs(x,y):
    if x < 0 or y < 0 or x >= n or y >= n or graph[x][y] == 0:
        return
    global apt
    #방문 처리
    graph[x][y] = 0
    apt += 1

    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x,y-1)


dangi = 0
apartments = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            apt = 0
            dangi += 1
            dfs(i,j)
            apartments.append(apt)

apartments.sort()
print(dangi)
for i in apartments:
    print(i)