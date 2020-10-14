init_loc = input()

moves = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
row = int(init_loc[1])
col = int(ord(init_loc[0])) - int(ord('a')) + 1 #영어 컬럼을 숫자로 바꾼다.

result = 0

for move in moves:
    nrow = row + move[1]
    ncol = col + move[0]
    if nrow >= 1 and ncol >= 1 and nrow <= 8 and ncol <= 8:
        result += 1
print(result)