#아이디어를 떠올리기 쉽지 않은 문제
#다양한 유형의 그리디를 많이 풀어봐야 한다.
#
n = int(input())
coins = list(map(int, input().split()))

#일단 정렬해
coins.sort()

target = 1
for x in coins:
    if target < x:
        break
    target += x

print(target)



