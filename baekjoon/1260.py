from collections import deque

n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for node in graph:
    node.sort()

visited = [False] * n

def dfs(graph, start):
    if visited[start -1]:
        return

    visited[start - 1] = True
    print(start, end=' ')

    for next_node in graph[start]:
        dfs(graph, next_node)

def bfs(graph, start):
    q = deque()
    q.append(start)
    visited[start - 1] = True
    print(start, end=' ')
    while q:
        now = q.popleft()

        for next_node in graph[now]:
            if not visited[next_node -1]:
                q.append(next_node)
                visited[next_node -1] = True
                print(next_node, end=' ')

dfs(graph, v)
print()
visited = [False] * n
bfs(graph, v)
