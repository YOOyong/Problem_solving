#가려는 곳이 모두 같은 집합이면 여행이 가능하다


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

n, m = map(int, input().split())
#부모 테이블 초기화
parent= [0] * (n+1)
#부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

#연결상태 입력을 받아 유니온 연산.
for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1 ,j+1)
#계획 입력 받기
plan = list(map(int,input().split()))

result = True

for i in range(m -1):
    #부모를 비교하여 하나라도 같지 않은게 있으면 false로
    if find_parent(parent,plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

if result:
    print('YES')
else:
    print('NO')
