def solution(n, numlist):
    return [numlist[i] for i in range(len(numlist)) if numlist[i] % n == 0]