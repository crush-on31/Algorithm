def solution(absolutes, signs):
    a = [absolutes[i] if signs[i] else -absolutes[i] for i in range(len(signs))]
    return sum(a)