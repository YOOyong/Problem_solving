# N(2 <= n <= 1000) M(1 <= m <= 10000) K(1 <= k <= 10000)    K >= M
# N개의 자연수 (1 <= x <= 10000)

n,m,k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse = True)
first = data[0]
second = data[1]

answer = 0

while True:
    #같은 수를 최대 k번 더할 수 있음.
    for i in range(k):
        if m == 0:
            break
        answer += first
        m -= 1
    if m == 0:
        break
    answer += second #두번째로 큰 수 한번 더하기
    m -= 1

print(answer)

