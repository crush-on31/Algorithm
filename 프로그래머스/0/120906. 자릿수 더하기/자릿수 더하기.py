def solution(n):
    answer = str(n)
    result = []
    a = 0
    for i in range(len(answer)):
        result.append(answer[i])
    for j in result:
        a += int(j)
    return a