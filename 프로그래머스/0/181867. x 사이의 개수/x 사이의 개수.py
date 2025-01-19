def solution(myString):
    a, b = [], []
    a += myString.split('x')
    for i in range(len(a)):
        b.append(len(str(a[i])))
    return b