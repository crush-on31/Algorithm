def solution(num_list):
    a = 0
    b = 0
    for x in range(len(num_list)): 
        if num_list[x] % 2 == 0:
            a += 1
        else:
            b += 1
        answer = [a,b]
        x += 1
    return answer