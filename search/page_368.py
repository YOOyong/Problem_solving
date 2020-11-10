#고정점 찾기
#고정점이란 수열의 원소중에서 그 값이 인덱스와 동일한 원소.
#숫자가 커서 이진탐색이 필요해.

n = int(input())
array = list(map(int,input().split()))

#array는 오름차순 정령
#array[mid]를 보는데 얘가 자기 인덱스보다

start = 0
end = n - 1
def binsearch():
    start = 0
    end = n -1
    while start <= end:
        mid = (start + end) // 2
        if mid == array[mid]:
            return mid
        elif mid > array[mid]:
            start = mid + 1
        else:
            end = mid -1

    return -1

print(binsearch())
