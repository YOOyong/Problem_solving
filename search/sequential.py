#원소를 순차적으로 탐색
array = [2,3,5,23,7,8,6,16,9,0]
def sequential_search(target, array):

    for i in range(len(array)):
        if array[i] == target:
            return i


print(sequential_search(8,array))

#O(N)