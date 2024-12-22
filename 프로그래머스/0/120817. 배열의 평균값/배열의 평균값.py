def solution(numbers):
    a = len(numbers)
    answer = 0
    for i in range(a):
        answer += numbers[i]
        i += 1
    b = answer / a
    return b