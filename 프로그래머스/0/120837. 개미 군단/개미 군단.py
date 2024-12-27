def solution(hp):
    a, b, c = hp % 5, hp % 3, hp % 1
    d, e, f = hp // 5, hp // 3, hp // 1
    if a == 0:
        return d
    elif a == 1 or a == 2:
        return d + ((hp-(5*d)) // 1)
    elif a == 3:
        return d + ((hp-(5*d)) // 3)
    else:
        return d + ((hp-(5*d)) // 3) + 1