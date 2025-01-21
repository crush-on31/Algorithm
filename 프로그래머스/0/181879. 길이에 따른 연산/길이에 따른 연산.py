def solution(num_list):
    a = 1
    for i in num_list:
        if len(num_list) > 10:
            a = sum(num_list) 
        else:
            a *= i
    return a