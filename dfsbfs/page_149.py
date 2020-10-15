#dfs 갈 수 있을 때 까지 가고 마지막에 리턴한다
n, m = map(int, input().split())

graph = list()
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1

        #모든 방향에 대해 재귀호출
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)

        return True
    return False

#모든 위치에 음료수 붓기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:# dfs는 이미 얼었거나 틀에 대해선 false를 반환한다.
                            # 재귀적으로 빈곳을 계속 채우면서 최종적으로 True가 나오면 답 + 1
            result += 1
print(result)