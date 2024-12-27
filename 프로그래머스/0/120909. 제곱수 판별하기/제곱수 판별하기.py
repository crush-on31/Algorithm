def solution(n):
    a = []
    for i in range(1001):
        a.append(i**2)
    if n in a:
        return 1
    else:
        return 2