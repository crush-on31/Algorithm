def solution(my_string):
    a = []
    for i in range(0,101):
        a.append(str(i))
    c = [int(j) for j in my_string if j in a]
    return sorted(c)