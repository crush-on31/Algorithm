def solution(s1, s2):
    s1_ = set(s1)
    s2_ = set(s2)
    answer = s1_ & s2_
    return len(answer)