def solution(myString):
    low = [i for i in 'abcdefghijk']
    return ''.join(['l' if j in low else j for j in myString])