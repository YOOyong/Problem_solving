numbers = list(map(int, list(input())))

answer = numbers[0]
for i in range(1, len(numbers)):

    if numbers[i] <= 1 or answer == 0:
        answer += numbers[i]
    else:
        answer *= numbers[i]

print(answer)