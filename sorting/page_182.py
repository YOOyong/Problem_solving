n, k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse= True)

for i in range(k):
    if A[i] < B[i]: #A가 작은 경우에만 바꾸어야 해!! 큰데 바꾸면 최대값이 안나옴.
        A[i], B[i] = B[i], A[i]
    else:# a의 첫 수가 b보다 큰경우엔 더 볼거없이 a만 더하는게 좋다.
        break

print(sum(A))
