def solution(my_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = [i for i in alpha] + [j for j in alpha.lower()]
    li = [int(k) for k in (len(answer)*'0')]
    for j in range(len(answer)):
        for i in my_string:
            if i == answer[j]:
                li[j] += 1
    return li