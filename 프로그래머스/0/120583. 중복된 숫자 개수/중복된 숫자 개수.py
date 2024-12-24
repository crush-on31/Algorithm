def solution(array, n):
    a = 0
    for i in range(len(array)):
        if array[i] == n:
            a += 1
    return a