def solution(a, b):
    if (a+b) % 2 == 0:
        if a % 2 == 0:
            if a-b >= 0:
                return a-b
            else:
                return -(a-b)
        else:
            return a**2 + b**2
    else:
        return 2*(a+b)