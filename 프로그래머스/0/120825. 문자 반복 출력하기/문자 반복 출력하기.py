def solution(my_string, n):
    if len(my_string) == 2:
        a = my_string[0]*n + my_string[1]*n
    elif len(my_string) == 3:
        a = my_string[0]*n + my_string[1]*n + my_string[2]*n
    elif len(my_string) == 3:
        a = my_string[0]*n + my_string[1]*n + my_string[2]*n + my_string[3]*n
    else:
        a = my_string[0]*n + my_string[1]*n + my_string[2]*n + my_string[3]*n + my_string[4]*n
    return a