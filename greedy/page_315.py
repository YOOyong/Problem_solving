n, m = map(int, input().split())
data = list(map(int,input().split()))

array = [0] * 11 #무게를 담을 리스트

for x in data:
    array[x] += 1

answer = 0

for i in range(1, m + 1):
    n -= array[i]
    answer += array[i] * n

print(answer)