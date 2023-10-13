def solution(x, y):
    m, f = int(x), int(y)
    generations = 0
    while m > 0 or f > 0:
        if m < 1 or f < 1:
            break
        if(m == 1 and f ==1 ):
            return str(generations)
        if(m > f):
            if(f > 1):
                division = m//f
                m = m - f * (division)
                generations += division 
            else:
                m = m - f
                generations +=1
        else:
            if(m > 1):
                division = f//m
                f = f - m * (division)
                generations += division
            else:
                f = f - m
                generations +=1
    if( m==1 and f ==1):
        return str(generations)
    else:
        return "impossible"

print(solution("2","1"))    

