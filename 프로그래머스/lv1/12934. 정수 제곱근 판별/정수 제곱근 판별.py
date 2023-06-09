# import math

# def solution(n):
#     sqrt = math.sqrt(n)
#     if sqrt - int(sqrt) == 0:
#         answer = int(math.pow(sqrt+1,2))
#     else:
#         answer = -1
#     return answer

def solution(n):
    sqrt = n**(1/2)
    if sqrt % 1 == 0:
        return (sqrt+1)**2
    return -1