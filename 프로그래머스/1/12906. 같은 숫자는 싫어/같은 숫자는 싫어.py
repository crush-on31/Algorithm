def solution(arr):
    answer = []
    #현재 인덱스 앞 또는 뒤의 결과 비교
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
    answer.append(arr[-1])
    return answer