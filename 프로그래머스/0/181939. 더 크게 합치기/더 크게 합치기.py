def solution(a, b):
    return max(a*(10**len(str(b)))+b, b*(10**len(str(a)))+a)