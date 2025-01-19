def solution(arr1, arr2):
    a = len(arr1) - len(arr2)
    b = sum(arr1) - sum(arr2)
    if a > 0:
        return 1
    elif a == 0:
        if b > 0:
            return 1
        elif b == 0:
            return 0
        else:
            return -1
    else:
        return -1