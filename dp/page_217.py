x = int(input())

d = [0] * (x + 1)
#d에 있는 값은 해당 수까지 오는 최소 연산 수
for i in range(2, x + 1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])