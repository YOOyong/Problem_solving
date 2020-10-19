n, m = map(int, input().split())
cakes= list(map(int, input().split()))

#적어도 M만큼의 떡을 가져가도록 하는 높이의 최댓값
start = 0
end = max(cakes)

answer = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    #떡 길이 계산
    for cake in cakes:
        if cake > mid: #떡을 자를 수 있을 때만
            total += cake - mid
    #양이 부족하다 (end를 내린다)
    if total < m:
        end = mid - 1
    #충분하다
    else:
        answer = mid  #답을 기록하고
        start = mid + 1 #최적의 해가 있나 또 탐색.

print(answer)
#이진탐색의 끝은 정해져있기 때문에 '답과 같다' 조건은 필요가 없다.