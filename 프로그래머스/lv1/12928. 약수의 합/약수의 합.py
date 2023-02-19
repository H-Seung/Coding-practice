# def solution(n):
#     result = 0
#     for i in range(1,int(n**0.5)+1):
#         if n % i == 0:
#             result += i + n/i
#     return result

# print(solution(16))

def solution(n):
    li = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            li.extend([i, n/i])
    return sum(list(set(li)))

print(solution(16))