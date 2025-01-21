def solution(arr):
    a = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            a.append(i // 2)
        elif i <=50 and i % 2 == 1:
            a.append(i * 2)
        else:
            a.append(i)
    return a