n, m = map(int, input().split())
x, y, d = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

is_visit = [[0] * m for _ in range(n)]
is_visit[x][y] = 1

#d / 0 N , 1 E, 2 S, 3 W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn(): #회전함수
    global d
    d -= 1 #왼쪽으로는 -1
    if d == -1: #한바퀴 다 돌게되면 초기화
        d = 3
answer = 1
turn_count = 0 #턴 횟수 변수로 방향을 다 봤나 체크 해야함.
while True:
    #돌고 시작
    turn()
    #왼쪽의 좌표
    nx, ny = x + dx[d], y + dy[d]
    if is_visit[nx][ny] == 0 and array[nx][ny] == 0 : #가려는 좌표가 간적이 없고 바다가 아님
        x, y = nx, ny #이동
        is_visit[x][y] = 1
        answer += 1   #이동 횟수 추가
        turn_count = 0 #이동하면 턴 횟수 초기화
        continue
    else: #가봤거나 바다이면 돌기만 한다.
        turn_count += 1
        #여기 컨티뉴하면 안됨. 여기서 턴카운트 올리면서 사방을 탐색하고,
    if turn_count == 4:  #네번 다 돌아봤다. (현재 위치에서 더 갈 곳이 없다)
        nx, ny = x - dx[d], y - dy[d]
        if array[nx][ny] == 0: #뒤가 갈 수 있는 곳
            x, y = nx, ny
        else:                  #갈수 없는 곳
            break
        turn_count = 0 #턴 횟수를 초기화

print(answer)

