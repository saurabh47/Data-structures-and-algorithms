def solution(x):
    count = 0
    n = int(x)
    while(n!=1):
        if(isEven(n)):
            n = n // 2
        else:
            # handle case for n = 3 since 3-1 = 2 and 3-2 = 1
            # 2 & 1 = 0 and 4 & 3 = 0
            if ((n+1 & n) > (n-1 & n-2) or (n == 3)):
                n = n-1
            else:
                n = n + 1
        count +=1
    return count

def isEven(n):
  return n % 2 ==0