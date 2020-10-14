# N x M 행렬
#행별로 입력
n , m = map(int, input().split())

min_list = []
for i in range(n):
    data = list(map(int, input().split()))
    min_list.append(min(data))

answer = max(data)
print(answer)