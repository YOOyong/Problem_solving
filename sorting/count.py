#계수정렬
array = [5,7,9,0,1,9,3,1,7,5,6,2,8,4,8]
#모든 범위를 포함하는 리스트 선언
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1
    
for i in range(len(count)):
    for j in range(count[i]): #숫자가 카운트된 수만큼 해당 수 프린트
        print(i, end=' ')