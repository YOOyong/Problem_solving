#큰 문제를 작은 문제로 나눌 수 있다
#작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다. (이미 해결한 문제를 다시 해결하는 경우가 있다)
#점화식 세우기(n부터 뒤로 보며 답이 나오는 경우를 살피자)

#대표예제 피보나치수열

memo = [0] * 100 #memoization을 위한 리스트 초기화

def fibo(x):
    if x == 1 or x == 2:
        return 1
    #이미 계산된 결과가 있다면 그걸 리턴
    if memo[x] != 0:
        return memo[x]
    #그게 아니라면 계산.
    memo[x] = fibo(x-1) + fibo(x -2)
    return memo[x]

print(fibo(99))

memo = [0] * 10

def pibo(x):
    print('f('+str(x) + ')', end= ' ')
    if x == 1 or x == 2:
        return 1
    if memo[x] != 0:
        return memo[x]
    memo[x] = pibo(x- 1) + pibo(x- 2)
    return memo[x]
print(pibo(8))



def piboBottomUp(x):
    memo = [0] * 100
    memo[1] = 1
    memo[2] = 1

    for i in range(3, x+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[x]

print(piboBottomUp(8))