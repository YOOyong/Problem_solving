# Knapsack 알고리즘.
# 배낭싸기. 무게와 가치가 따로 주어지고 최대로 가져갈 수 있는 가치는?
# dp문제
n, k = map(int, input().split())

w = [] #무게 리스트
v = [] #가치 리스트
for _ in range(n):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

d = [0] * (k + 1) # d[i]는 i 무게를 가지는 가방에 넣을 수 있는 최대가치
# case1  i번째 보석을 가져간 경우
# case2  i번째 보석을 가져가지 않는 경우
"""
case 1
    d[k] = d[k - w[i]] + v[i]
    
case 2 
    d[k] = d[k]

물건을 하나씩 검사하며 dp 테이블은 역순으로 돌며 각 가방에 넣을지 안넣을지를 결정.
무게 k 가방에서 max(d[k], d[k] = d[k - w[i]] + v[i]) 실행
"""
for i in range(n):
    for j in range(k, 0, -1):
        if w[i] <= j: #i번째 물건의 무게와 가방의 크기를 비교해 넣을 수 있으면
            d[j] = max(d[j], (d[j - w[i]] + v[i]))

print(d[k])








