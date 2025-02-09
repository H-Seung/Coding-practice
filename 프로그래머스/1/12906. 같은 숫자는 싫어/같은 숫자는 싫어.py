def solution(arr):
    answer = []
    for v in arr:
        if answer == []:
            answer.append(v)
        if v != answer[-1]:
            answer.append(v)
    
    return answer