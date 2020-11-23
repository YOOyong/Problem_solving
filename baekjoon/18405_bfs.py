#bfs로 하면 될듯

#아래 방법 말고 큐에 좌표, 시간을 같이 저장하는 방법도 생각해보자.
#큐에 (s,x,y) 식으로 쓰는 것. 바이러스를 퍼뜨리고 추가할 때는 (s+1, x,y) 식으로 q에 append
#while 시작부분에  초 검사해서 입력시간이면 break
from _collections import deque
n, k = map(int, input().split())

graph = [[0] for _ in range(n+1)]
for i in range(n):
    graph[i+1].extend(list(map(int,input().split())))

time, final_x, final_y = map(int,input().split())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

virus_list = [[] for _ in range(k+1)]

for x in range(1,n+1):
    for y in range(1,n+1):
        if graph[x][y] == 0:
            continue
        index = graph[x][y]
        virus_list[index].append((x,y))
temp = []
for viruses in virus_list:
    temp.extend(viruses)

q = deque(temp)
sec = 0
count = 0
while q:
    if sec == time:
        break
    x, y = q.popleft()
    virus = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 1 or ny < 1 or nx >= n+1 or ny >= n+1: # 벗어난 범위 무시
            continue
        if graph[nx][ny] != 0: #바이러스가 이미 있는경우 무시
            continue
        graph[nx][ny] = virus #바이러스 퍼뜨리기.
        q.append((nx, ny))

    #시간보내기 위해 다음 큐를 미리 받아놓음.(큐가 비어있는 경우도 있어서 else처리함)
    if q:
        tempx, tempy = q[0]
    else:
        break

    if virus != graph[tempx][tempy]: # 다음 차례의 바이러스종류가 바뀔 때 마다 카운트 + 1
        count += 1
    if count == k-1:  #카운트가 바이러스의 종류 개수 -1 개이면 1초가 지난걸로 처리.
        sec += 1
        count = 0 #1초가 지나면 카운트 리셋.


print(graph[final_x][final_y])
