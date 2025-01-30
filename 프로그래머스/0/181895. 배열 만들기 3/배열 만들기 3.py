def solution(arr, intervals):
    a, b = intervals[0], intervals[1]
    if not (a[1]+1):
        answer = arr[a[0]:a[-1]]+arr[b[0]:b[1]+1]
    elif not (b[1]+1):
        answer = arr[a[0]:a[1]+1]+arr[b[0]:b[-1]]
    elif not (a[1]+1) and (b[1]+1):
        answer = arr[a[0]:a[-1]]+arr[b[0]:b[-1]]
    else:
        answer = arr[a[0]:a[1]+1]+arr[b[0]:b[1]+1]
    return answer