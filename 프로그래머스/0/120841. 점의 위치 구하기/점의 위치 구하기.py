def solution(dot):
    a = dot[0]
    b = dot[1]
    if a > 0 and b > 0:
        return 1
    elif a < 0 and b > 0:
        return 2
    elif a < 0 and b < 0:
        return 3
    else:
        return 4