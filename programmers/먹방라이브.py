"""
모든 음식을 시간순으로 정렬한뒤에 빨리 먹을 수 있는것부터 없애는 식으로 하면 됨
"""
import heapq
def solution(food_times, k):

    #전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    q = []
    #(음식시간, 음식번호)형으로 우선순위 큐에 삽입.
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 #먹기위해 사용한 시간.
    pre = 0 #직전에 다 먹은 음식의 시간

    length = len(food_times) #남은 음식의 개수
    while sum_value + ((q[0][0] - pre) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - pre) * length
        length -= 1
        pre = now

    result = sorted(q, key = lambda x: x[1])
    return result[(k-sum_value) % length[1]]



"""
초를 보내면서 먼저 0인지 확인하며 0이 아닌 인덱스로 이동.
다 돌아도 0이면 바로 -1 리턴.
먹는다.
인덱스 최신화.
순으로 했는데 일부 맞고 일부 틀리고,
효율성 검사 전부 탈락.
"""

def solution(food_times, k):
    answer = 0
    index = 0
    for _ in range(k): # 시간 보내기
        #0이 아닌 인덱스까지 인덱스를 늘린다.
        count = 0
        while food_times[((index % len(food_times) - 1) + 1)] == 0:
            if count == len(food_times):
                return -1
            index += 1
            count += 1


        #먹는다.
        food_times[((index % len(food_times) - 1) + 1)] -= 1
        #인덱스 늘리기.
        index += 1
        count = 0


    answer = ((index % len(food_times) - 1) + 1) + 1

    if sum(food_times) == 0:
        return -1
    else:
        return answer