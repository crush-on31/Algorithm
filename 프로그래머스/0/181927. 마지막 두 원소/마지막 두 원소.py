def solution(num_list):
    a, b = num_list[-1], num_list[-2]
    num_list.append(a-b) if a > b else num_list.append(a*2)
    return num_list