def solution(n):
    s = '수박'*(n//2)
    if n%2==1:
        s=s+'수'
    return s
