def solution(x):
    count = 0
    n = int(x)
    while(n!=1):
        if(isEven(n)):
            n = n // 2
        else:
            if ((n+1 & n) > (n-1 & n-2) or (n == 3)):
                n = n-1
            else:
                n = n + 1
        count +=1
    return count

def isEven(n):
  return n % 2 ==0