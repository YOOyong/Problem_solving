n, x = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = len(array)
answer = 0

while start <= end:
    mid = (start+ end) // 2
    if array[mid] == x and array[mid-1] != x:
        x_start = mid
    elif array[mid] > x:
        end = mid - 1
    else:
        start = mid + 1