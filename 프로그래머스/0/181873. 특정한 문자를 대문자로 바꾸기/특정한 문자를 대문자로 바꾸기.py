def solution(my_string, alp):
    a = [i.upper() if i == alp else i for i in my_string]
    return ''.join(a)