# reshape가 쉽도록 넘파이를 이용한 풀이
# out of index를 막기위해 memo 매트릭스에 아래 위 한줄씩 패딩을 더함.
import numpy as np

n, m = map(int, input().split())
mine = np.array(list(map(int, input().split()))).reshape((n, m))
gold = np.zeros((n+2, m))

def dig():
    for i in range(n): #첫 열을 채우기
        gold[i+1][0] = mine[i][0]

    # for i in range(n): #둘째 열을 계산하여 채우기.
    #     gold[i+1][1] = max(gold[i+1][0] + mine[i][1],  gold[i][0] + mine[i][1], gold[i+2][0] + mine[i][1])
    #이부분은 쓸데 없는데 해놓고 아래서 j의 레인지를 (2,m) 으로 했다.


    #나머지 전체를 계산.
    for i in range(n):
        for j in range(1, m):
            gold[i+1][j] = max(mine[i][j] + gold[i+1][j-1], mine[i][j] + gold[i][j-1], mine[i][j] + gold[i+2][j-1])
            #gold[i+1][j] = mine[i][j] + max(gold[i+1][j-1], gold[i][j-1], gold[i+2][j-1]) 이렇게 쓰는게 더 이쁘다.
    return int(np.max(gold))

print(dig())

#답 풀이.
#여기서는 테스트 케이스 받는 부분까지 있음.
#dp 테이블 자체를 갱신하며 문제를 푼다.

#테스트 케이스 입력
# for tc in range(int(input())):
#
#     #금광 정보 입력
#     n,m= map(int,input().split())
#     array= list(map(int,input().split()))
#
#     #dp 테이블 만들기.
#     dp = []
#     index = 0
#     #array를 한줄 리스트로 줬기 때문에 이런식으로 받아야 한다.
#     for i in range(n):
#         dp.append(array[index:index + m])
#         index += m
#
#     #dp 진행.
#
#     for j in range(1, m):
#         for i in range(n):
#             #왼쪽 위에서 오는 경우
#             if i == 0:
#                 left_up = 0
#             else:
#                 left_up = dp[i-1][j-1]
#
#             #왼쪽에서 오는 경우
#             left = dp[i][j-1]
#
#             #왼쪽 아래에서 오는 경우
#             if i == n - 1:
#                 left_down = 0
#             else:
#                 left_down = dp[i+1][j-1]
#
#             dp[i][j] = dp[i][j] + max(left, left_down, left_up)
#
#     result = 0
#     for i in range(n):
#         result = max(result, dp[i][m -1])
#     print(result)

