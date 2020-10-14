n, k = map(int, input().split())
answer = 0
while n != 1:
    if n >= k and n % k == 0:
        n = n / k
        answer += 1
    else:
        n -= 1
        answer += 1

print(answer)