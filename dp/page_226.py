n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

#d에는 각 인덱스를 구성하는 최소의 경우가 들어가도록 한다

d[0] = 0
for coin in array:
    for j in range(coin, m + 1):
        if d[j - coin] != 10001:# 이 조건은 필요는 없지만 이해를 위해.
            d[j] = min(d[j], d[j - coin] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])