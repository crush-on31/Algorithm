def solution(numbers):
    numbers.sort()
    a = len(numbers)
    
    return numbers[a-1]*numbers[a-2]