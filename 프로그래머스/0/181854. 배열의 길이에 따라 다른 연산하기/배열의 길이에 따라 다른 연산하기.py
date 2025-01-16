def solution(arr, n):
    a = []
    num = len(arr[::2])
    if len(arr) % 2 != 0:
        for i in range(num-1):
            a.append(n + arr[2*i])
            a.append(arr[(2*i)+1])
        a.append(n + arr[-1])
    else:
        for i in range(num):
            a.append(arr[2*i])
            a.append(n + arr[2*i+1])     
    return a