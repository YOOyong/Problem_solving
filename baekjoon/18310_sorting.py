#이진탐색 그런 문제가 아니라 중간값이면 항상 최소가 된다는것 알아채야한다
#결국 리스트의 중간값을 구라하는 것
n = int(input())
houses = list(map(int, input().split()))

houses.sort()

print(houses[(n - 1) // 2])
