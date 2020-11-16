#뱀문제는 맹의 위치를 그래프에도 표시하고, 좌표를 전부 큐에 저장한다.
#뱀이 이동할때 머리를 이동하고, 큐에서 팝하여 꼬리를 제거.하면 됨.
n= int(input()) #맵 크기
k = int(input()) #사과의 개수

graph = [[0] * (n+1) for _ in range(n+1)]

#사과 입력
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

#움직임 입력
l = int(input())
move_set = []
for _ in range(l):
    sec, d = input().split()
    move_set.append((int(sec), d))

#처음에는 오른쪽을 보고있으므로 (동남서북)의 순서로.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, command):
    if command == 'L': #왼쪽 회전
        direction = (direction -1) % 4
    else:  #오른쪽 회전
        direction = (direction +1) % 4
    return direction

def simulate():
    #시뮬레이션 초기값들.
    x, y = 1, 1 #뱀 시작위치
    graph[x][y] = 2 #뱀은 2로 표시
    direction = 0
    time = 0 #지난 시간
    index = 0 #move_set 인덱스
    q = [(x,y)] #뱀의 좌표를 큐에 저장. 왼쪽이 꼬리.

    #시뮬 돌리기
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and 1 <= ny and nx <= n and ny <= n and graph[nx][ny] != 2:
            #사과 없는경우
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2 #뱀위치 업데이트
                q.append((nx,ny)) #큐에 뱀 추가
                px, py = q.pop(0) #꼬리좌표
                graph[px][py] = 0 #꼬리부분 이동처리
            #사과 있는경우
            if graph[nx][ny] == 1:
                #사과가 있는경우엔 꼬리를 그대로 둔다
                graph[nx][ny] = 2
                q.append((nx,ny))
        else: #벽이나 자기 몸에 닿은 경우
            time += 1
            break
        x, y = nx, ny #현위치 업데이트
        time += 1
        if index < l and time == move_set[index][0]:
            direction = turn(direction , move_set[index][1])
            index += 1
    return time

print(simulate())






