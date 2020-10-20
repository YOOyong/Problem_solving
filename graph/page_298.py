n, m = map(int, input().split())

#parent 초기화
parent = [0] * (n + 1)
for i in range(n):
    parent[i] = i

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

answer = []
for _ in range(m):
    op, a, b = map(int, input().split())

    if op == 1:
        #같은 팀 여부 확인
        if find_parent(parent, a) == find_parent(parent, b):
            answer.append('YES')
        else:
            answer.append('NO')
    else:
        union_parent(parent, a, b)

for x in answer:
    print(x)