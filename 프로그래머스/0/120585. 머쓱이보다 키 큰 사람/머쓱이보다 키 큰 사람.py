def solution(array, height):
    a = 0
    for i in range(len(array)):
        if (array[i] > height) == True:
            a += 1
    return a