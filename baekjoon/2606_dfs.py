n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * n
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

count = -1


def dfs(graph, start):
    if visited[start-1]:
        return
    global count
    visited[start-1] = True
    count += 1
    for next_node in graph[start]:
        dfs(graph, next_node)

dfs(graph, 1)

print(count)


