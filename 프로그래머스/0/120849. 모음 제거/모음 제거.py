def solution(my_string):
    see = ['a', 'e', 'i', 'o', 'u']
    a = [i for i in my_string if i not in see]
    return ''.join(a)