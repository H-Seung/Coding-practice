def solution(t, p):
    answer = 0
    parts = []
    
    for i in range(len(t)-len(p)+1):
        parts.append(t[i:len(p)+i])
    print(parts)
    
    for part in parts:
        if part <= p:
            answer += 1
    
    return answer