def solution(my_string, is_prefix):
    answer = [my_string[:i] for i in range(len(my_string))]
    return int(is_prefix in answer)