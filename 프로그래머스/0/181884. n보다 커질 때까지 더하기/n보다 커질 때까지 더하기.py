def solution(numbers, n):
    a = 0
    for i in range(len(numbers)):
        a = sum(numbers[:i+1])
        if a > n:
            break
    return a