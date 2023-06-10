def solution(s):
    tmp = s.lower()
    if tmp.count('p') == tmp.count('y'):
        return True
    else:
        return False