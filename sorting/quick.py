#호어분할
array = [5,7,9,0,3,1,6,2,4,8]

def qsort(array, start, end):
    if start >= end: #원소가 한개인 경우
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        #각 조건에 맞는 값이 나올때 까지 포인터 조정
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right >= start and array[start] >= array[pivot]:
            right -= 1

    if left > right:#포인터가 엇갈렸다면
        array[right], array[pivot] = array[pivot] = array[right]
    else:           #엇갈리지 않았다면
        array[left], array[right] = array[right], array[left]

    qsort(array, start, right-1)
    qsort(array, right+1, end)

def quick(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    left = [x for x in list[0:] if x < pivot]
    right = [x for x in list[0:] if x > pivot]
    return quick(left) + [pivot] + quick(right)

print(quick(array))