def solution(my_string, indices):
    mine, hint = [i for i in my_string],[j for j in range(len(my_string)) if j not in sorted(indices)]
    return ''.join([mine[j] for j in hint])