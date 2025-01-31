def solution(s):
    answer = []
    for i in range(len(s)):
        a = -1
        for j in range(0,i):
            if s[j] == s[i]:
                a = i-j
            
        answer.append(a)
                
    return answer