def solution(n):
    li = [n]
    while li[-1] != 1:
        li.extend([int(li[-1] / 2 if li[-1] % 2 == 0 else (3*li[-1])+1)])
    return li