def solution(s):
    # substr은 문자열의 길이를 반으로 나눈 값을 최대로 하면 된다.
    answer = len(s)
    for step in range(1, len(s) // 2+ 1):
        # cut 개수만큼 슬라이싱 하고 순환.
        newstring = ""
        prev = s[0:step] # 앞에서 step만큼의 문자열 추출
        count = 1
        for j in range(step, len(s), step):
            #이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j : j+step]:
                count += 1
            #다른 문자열이 나왔다면
            else:
                newstring += str(count) + prev if count >= 2 else prev #두번 이상 반복일때만 숫자 쓰기
                prev = s[j: j+step]
                count = 1

        #남아있는문자열 처리
        newstring += str(count) + prev if count >= 2 else prev

        answer = min(answer, len(newstring))

    return answer

