def solution(my_string, s, e):
    target = list(my_string[s:e+1])
    target.reverse()
    return my_string[:s] + ''.join(target) + my_string[e+1:]