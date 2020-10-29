import sys
sys.setrecursionlimit(100000) #재귀 깊이 에러 방지

t = int(input())
answers = []

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m or graph[x][y] == 0:
        return
    graph[x][y] = 0

    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x-1, y)
    dfs(x, y-1)

#테스트 케이스 만큼 입력 받기
for _ in range(t):
    m, n, k = map(int,input().split())
    graph = [[0] * m for _ in range(n)]

    #배추 심기
    for _ in range(k):
        a, b = map(int,input().split())
        graph[b][a] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i,j)
                count += 1

    answers.append(count)

for i in answers:
    print(i)