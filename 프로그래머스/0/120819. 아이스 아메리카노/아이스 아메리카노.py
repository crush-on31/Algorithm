def solution(money):
    answer = money // 5500
    an = money % 5500
    return [answer, an]