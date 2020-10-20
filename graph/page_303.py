from collections import deque
n = int(input())
import copy

graph = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    temp_list = list(map(int, input().split()))
    time[i] = temp_list[0] #시간 저장
    for x in temp_list[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        max_time = 0
        for next in graph[now]:
            result[next] = max(result[next], result[now] + time[next])
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(now)

    for i in range(1, n + 1):
        print(result[i])