s = input()
#0으로 바꾸는 경우와  1로 바꾸는 경우중 더 작은 수를 고르면 답이 된다.
#실제로 바꾸지 않고 횟수만 센다.

count0 = 0
count1 = 0

#첫번째 원소먼저 계산
if s[0] == '1':
    count0 += 1
else:
    count1 += 1

#두번째 원소부터 모든 원소를 확인
for i in range(len(s) - 1):
    #다음 원소와 다른경우 바뀜 카운트 늘림.
    if s[i] != s[i+1]:
        if s[i+1] == '1': #서로 다르고 다음게 1이면 0으로 바꾸는 경우 +1
            count0 += 1
        else:            #서로 다르고 다음게 0이면 1로 바꾸는 경우 +1
            count1 += 1

print(min(count0, count1))

