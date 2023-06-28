def solution(s):
    if len(s) % 2:  # 홀수
        return s[len(s)//2]
    elif not(len(s) % 2): # 짝수
        return s[len(s)//2-1]+s[len(s)//2]