def solution(arr, idx):
    a = [i for i in range(len(arr)) if (idx <= i and arr[i] == 1)]
    if a == []:
        return -1
    else:
        return a[0]