def solution(s):
    string = []
    parts = s.split(' ')
    for i in range(len(parts)):
        string.append(int(parts[i]))
    answer = f'{min(string)} {max(string)}'
    return answer
