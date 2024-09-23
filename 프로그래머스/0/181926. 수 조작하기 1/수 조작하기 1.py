def solution(n, control):
    dic = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))

    answer = n + sum([dic[c] for c in control])
    
    return answer
