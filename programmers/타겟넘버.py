def solution(numbers, target):
    answer = 0
    lenght = len(numbers)

    def dfs(idx, temp):
        if idx == lenght:
            if target == temp:
                nonlocal answer
                answer += 1
            return
        else:
            op = numbers[idx]
            dfs(idx+1, temp + op)
            dfs(idx+1, temp - op)

    dfs(0,0)

    return answer
