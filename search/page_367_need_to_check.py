#이 문제는 수가 반복되는 시작점과 끝점을 이진탐색으로 찾는 문제임.

n, x = map(int, input().split())
array = list(map(int, input().split()))
# x가 등장하는 횟수.
# x의 시작위치, 끝 위치를 알아내고
# answer =  right - left + 1
# 왜 안돌지????????????
def binsearch_left(target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if (mid == 0 or array[mid - 1] < target) and array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

def binsearch_right(target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start - end) // 2
        if (mid == (n-1) or  array[mid + 1] > target) and array[mid] == target:
            return mid
        elif array[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return None

temp = binsearch_left(x)

if temp != None:
    answer = binsearch_right(x) - temp + 1
    print(answer)
else:
    print(-1)

# 왜 안되는지는 다음에 알아보도록 하자.






