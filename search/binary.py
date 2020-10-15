#이미 정렬되어 있어야함.
#start, end, mid 필요

def bin_search_recursive(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return bin_search_recursive(array, target, start, mid-1)
    else:
        return bin_search_recursive(array, target, mid+1, end)

def bin_search_loop(array, target, start, end):
    while start <= end: #start가 end를 넘어가면 종료
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1 #끝점 바꾸기
        else:
            start = mid + 1 #시작점 바꾸기
    return None