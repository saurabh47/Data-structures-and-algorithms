# 0: 0, 3, 7, 11, 15
# 1: 1, 5, 9, 13,
# n+1: 2, 6, 10, 14, 18
# n: 4, 8, 12, 16, 20
def xor_n(x):
    if(x % 4 == 0):
        return x
    elif((x - 1) % 4 == 0):
        return 1
    elif((x - 2) % 4 == 0):
        return x+1
    else:
        return 0

def solution(start, length):
    result = 0
    col = length-1
    for i in range(length, 0, -1): # 4, 3
        end  = start + col
        result ^= (xor_n(start-1) ^ xor_n(end))
        col -=1
        start = start+length
    return result