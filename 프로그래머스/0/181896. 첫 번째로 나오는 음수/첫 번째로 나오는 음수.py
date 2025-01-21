def solution(num_list):
    a = [i for i in num_list if i < 0]
    if len(a) == 0:
        return -1
    else:
        return num_list.index(a[0])