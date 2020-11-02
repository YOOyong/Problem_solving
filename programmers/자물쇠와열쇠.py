#패딩까진 생각했는데 구현을 못함.
#솔루션에서 키를 넣는 부분을 아직 이해 못함.

def turn_key(key):
    n = len(key)  # 행
    m = len(key[0])  # 열
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = key[i][j]
    return result

def check(padded_lock):
    #시작점은 나누기 3해서 나온 값
    n = len(padded_lock)
    for i in range(n // 3):
        for j in range(n // 3):
            if padded_lock[i + (n//3)][j+(n//3)] != 1:
                return False
    return True

def solution(key, lock):
    locksize = len(lock)
    keysize = len(key)
    # 자물쇠에 패딩 넣기.
    padded_lock = [[0] * (locksize * 3) for _ in range(locksize * 3)]
    # 중간에 원본 lock 박기
    for i in range(locksize):
        for j in range(locksize):
            padded_lock[i + locksize][j + locksize] = lock[i][j]

    #키를 돌려가며 패디드 락에 키를 넣어가며 검사.
    for turn in range(4):
        key = turn_key(key)
        #시작점이 locksize * 2 면 모든 범위를 커버 가능.
        for i in range(locksize * 2):
            for j in range(locksize * 2):
                # 시작점에서 키 인덱스를 더하면 키 모양대로 padded_lock에 겹칠 수 있음.
                for x in range(keysize):
                    for y in range(keysize):
                        padded_lock[i + x][j + y] += key[x][y]
                if check(padded_lock):
                    return True

                for x in range(keysize):
                    for y in range(keysize):
                        padded_lock[i + x][j + y] -= key[x][y]

    return False





