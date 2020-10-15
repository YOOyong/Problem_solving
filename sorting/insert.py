array = [6,2,8,3,5,9,1]

for i in range(1, len(array)): #삽입정렬은 0번째 다음 부터 시작
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]: # 뒤에게 더 크면 자리 바꾸는걸 반복
            array[j], array[j-1] = array[j-1], array[j]
        else: #제 자리를 찾으면
            break

print(array)

#삽입정렬은 선택정렬과 같은 O(n^2)이지만 
#이미 어느정도 정렬되어있는 리스트에서는 좀 더 빠르다.
#최선의 경우 O(N)
#경우에 따라 큌정렬보다 빠를 수 있음.