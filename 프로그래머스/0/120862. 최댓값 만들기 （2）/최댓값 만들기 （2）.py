def solution(numbers):
    list = []
    for i in numbers:
        for j in numbers:
            if i != j:
                list.append(i*j)
    for k in numbers:
        if numbers.count(k) >= 2:
            list.append(k**2)
    return max(list)