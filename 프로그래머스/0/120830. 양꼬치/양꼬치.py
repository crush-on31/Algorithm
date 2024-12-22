def solution(n, k):
    a = n // 10
    if n >= 10:
        if a > 0:
            answer = 12000*n + 2000*(k-a)
            return answer
        else:
            answer = 12000*n + 2000*k
            return answer
    else:
        answer = 12000*n + 2000*k
        return answer