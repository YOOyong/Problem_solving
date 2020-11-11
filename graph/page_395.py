#순서대로 도킹시킨다.
#이걸 왜 유니온파인드로 풀어야 하는가를 이해해야

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a ,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a]= b

g = int(input())
p = int(input())

#parent 초기화
parent = [0] * (g+1)
#부모는 자기 자신으로 초기화
for i in range(g+1):
    parent[i] = i
count = 0
#비행기가 들어돌 때마다 바로 앞 게이트와 합집합 진행
for _ in range(p):
    gp = int(input())
    #부모가 0이면 비행기가 들어갈 수 없는 상태.
    if find_parent(parent, gp) == 0:
        break
    else:
        union_parent(parent, gp, gp-1)
        count += 1

print(count)
