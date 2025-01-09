def solution(rsp):
    dic = {'2':'0','0':'5','5':'2'}
    a = []
    for i in range(len(rsp)):
        a.append(dic[rsp[i]])
    return ''.join(a)