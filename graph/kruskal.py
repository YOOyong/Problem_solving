#최소비용 신장트리 찾기.

# 간선 데이터를 비용에 따라 오름차순 정렬
# 간선을 하나씩 확인하면서 현재의 간선이 사이클을 발생시키는지 확인
#     사이클이 발생하지 않는경우 최소신장트리에 포함시칸다
#     사이클이 발생하는 경우 최소신장트리에서 제외한다
# 모든 간선에 대해 이를 반복


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

#모든 간선을 담을 리스트
edges = []
result = 0

#부모테이블 초기화
for i in range(1, v+1):
    parent[i] = i

#간선정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split)
    #정렬을 위해 cost를 맨 앞으로 저장
    edges.append((cost, a, b))
#간선 정보 저장
edges.sort()

for edge in edges:  #모든 간선에 대해
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 유니온 수행
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)



