def solution(myString, pat):
    my = ''.join(['B' if i == 'A' else 'A' for i in myString])
    return int(pat in my)