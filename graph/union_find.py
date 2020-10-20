#서로소 집합
#union-find

# def find_parent(parent, x):
#     #해당 노드가 최상위 노드가 아니면
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     #최상위 노드일 때만 리턴
#     return x

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    #두 원소의 부모 찾기
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    #부모비교하여 더 큰 번호를 가진 애가 부모가 되게 함.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
#노드의 개수와 간선의 개수 입력받기
v, e =map(int, input().split())
parent = [0] * (v + 1)

#부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

#유니온 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
#각 원소가 속한 집합 출력
for i in range(1, v + 1):
    print(find_parent(parent, i), end = ' ')

#서로소 집합은 무방향그래프의 순환을 검사 할 수 있음
cycle = False
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle= True
        break
    else:
        union_parent(parent,a ,b)