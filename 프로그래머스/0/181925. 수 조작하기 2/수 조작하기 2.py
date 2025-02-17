def solution(numLog):
    result = []
    for i in range(len(numLog)-1):
        answer = numLog[i+1]-numLog[i]
        if answer == 1:
            result.append('w')
        elif answer == -1:
            result.append('s')
        elif answer == 10:
            result.append('d')
        else:
            result.append('a')
    return ''.join(result)