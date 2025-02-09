def solution(n_str):
    return [n_str[i:] for i in range(len(n_str)) if n_str[i] != '0'][0]