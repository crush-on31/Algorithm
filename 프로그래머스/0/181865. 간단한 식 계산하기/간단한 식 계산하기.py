def solution(binomial):
    bi = binomial.strip()
    if '+' in bi:
        a = bi.index('+')
        return int(bi[:a])+int(bi[a+1:])
    elif '-' in bi:
        a = bi.index('-')
        return int(bi[:a])-int(bi[a+1:])
    else:
        a = bi.index('*')
        return int(bi[:a])*int(bi[a+1:])