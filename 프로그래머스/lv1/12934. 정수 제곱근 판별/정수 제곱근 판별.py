import math

def solution(n):
    sqrt = math.sqrt(n)
    if sqrt - int(sqrt) == 0:
        answer = int(math.pow(sqrt+1,2))
    else:
        answer = -1
    return answer
