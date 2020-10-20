n = int(input())
array = list(map(int,input().split()))

array.sort()
answer = 0
count = 0

for i in array:
    count += 1
    if count >= i:
        answer += 1
        count = 0
print(answer)

