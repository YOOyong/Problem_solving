n = int(input())
stocks = list(map(int, input().split()))
m = int(input())
orders = list(map(int, input().split()))

#이진탐색을 위해 정렬
stocks.sort()

def bin_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


for order in orders:
    if bin_search(stocks, order, 0, len(stocks)):
        print('yes', end=' ')
    else:
        print('no', end=' ')