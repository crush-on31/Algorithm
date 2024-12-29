def solution(n):
    a = [x for x in range(1,n+1) if n % x == 0]        
    return len(a)