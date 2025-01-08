def solution(my_string):
    list = []
    for i in range(1,1001):
        list.append(f"{i}")
    a = 0
    for i in range(len(my_string)):
        if my_string[i] in list:
            a += int(my_string[i])
    return a