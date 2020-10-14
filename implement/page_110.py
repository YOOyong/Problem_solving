n = int(input())
plans = input().split()

#초기 좌표
x,y = 1,1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move = ['L', 'R', 'U', 'D']

for plan in plans:

    #이동 후 좌표를 일단 계산만 해놓는다.
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
