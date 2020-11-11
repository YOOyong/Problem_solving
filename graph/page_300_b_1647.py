#백준 1647
#최소비용신장트리를 찾는 크루스칼 알고리즘
n, m = map(int, input().split())

edges = []
parent = [0] * (n + 1)
for i in range(n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost =  map(int, input().split())
    edges.append((cost,a,b))

edges.sort()

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a ,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#크루스칼 알고리즘
result = 0
max = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        #최소비용 신장트리에 포함 될 때만 max를 바꾼다.
        #비용 기준으로 간선을 소팅했기 때문에 마지막에 넣는 값은 당연히 최대값이다.
        max = cost

print(result - max)

